from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import UserBank
from accounts.models import UserBankAccount
from .models import TransactionModel
from .forms import DepositForm, WithdrawForm, LoanRequestForm, TransferBalanceForm
from .constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, SEND_MONEY, RECIEVED_MONEY
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

def sendTransactionEmail(user, amount, subject,template):
    message = render_to_string(template,{
        'user': user,
        'amount': amount
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = TransactionModel
    title = ''
    success_url = reverse_lazy('transaction_report')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account, 
        })
        return kwargs
    
    #This method is used to populate a dictionary to use as the template context. 
    # You will probably be overriding this method most often to add things to display in your templates.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit' # built-in keyword na
    
    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial
    
    # if form.is_valid(): 
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        
        messages.success(self.request,f"{amount} $ was deposited to your account successfully!")
        
        sendTransactionEmail(self.request.user,amount,"Deposit Message",'deposit_email.html')
        
        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money' # built-in keyword na
    
    # Backend theke dekha jabe initially
    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial
    
    # if form.is_valid(): 
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        bank = UserBank.objects.get(bank_name="Mamar Bank")
        if bank.is_bankrupt == False:
            account.balance -= amount
            account.save(
                update_fields = ['balance']
            )
            messages.success(self.request,f"{amount} $ was withdrawn from your account successfully!")
            sendTransactionEmail(self.request.user,amount,"Withdrawal Message",'withdrawal_email.html')
        else:
            messages.error(self.request, f"Sorry! you can't withdraw money for this time. Because, Bank is Bankrupt now!")
            sendTransactionEmail(self.request.user,amount,"Withdrawal Failed Message",'failed_withdrawal_email.html')
            return redirect('transaction_report')
        return super().form_valid(form)
    
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan' # built-in keyword na
    
    # Backend theke dekha jabe initially
    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial
    
    # if form.is_valid(): 
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        
        # User'r kotogula laon approve hoise seita count korbo
        current_loan_count = TransactionModel.objects.filter(account= self.request.user.account, transaction_type= LOAN,loan_approve=True).count()
        
        if current_loan_count >=3 :
            return HttpResponse("You crossed your loan limit")
        messages.success(self.request,f"Loan request for {amount} $ has been successfully sent to admin!")
        
        sendTransactionEmail(self.request.user,amount,"Loan Request Message",'loan_email.html')
        
        return super().form_valid(form) # form taake amar jinishgula diye overright kore dilaam



class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transaction_report.html'
    model = TransactionModel
    balance = 0
    context_object_name = 'report_list'
    
    def get_queryset(self):
        # jodi user kono type filter na kore tahole taar total transaction report dekhabo!
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        start_date_str =  self.request.GET.get('start_date')
        end_date_str =  self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            queryset = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date)
            self.balance = TransactionModel.objects.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))
            ['amount_sum']
        else:
            self.balance = self.request.user.account.balance
        
        return queryset.distinct()
    
    # context hisebe 'account' ke pathabo!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })
        return context
    
class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(TransactionModel, id=loan_id)
        
        if loan.loan_approve: # akjon user loan pay korte paarbe tokhoni jokhon taar loan approve hobe!
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount # current balance theke loan amount baad disi!
                loan.balance_after_transaction = user_account.balance # balance after transaction ke current balance diye replace korlam!
                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('loan_list')
            else:
                messages.error(self.request,f"Loan amount is greater than available balance")
        return redirect('loan_list')
            
# class LoanListView(LoginRequiredMixin, ListView):
#     model = TransactionModel
#     template_name = 'loan_request.html'
#     context_object_name = 'loans'
    
#     def get_queryset(self):
#         user_account = self.request.user.account
#         queryset = TransactionModel.objects.filter(account=user_account,transaction_type=LOAN)
#         return queryset
class LoanListView(LoginRequiredMixin,ListView):
    model = TransactionModel
    template_name = 'loan_request.html'
    context_object_name = 'loans' # loan list ta ei loans context er moddhe thakbe

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = TransactionModel.objects.filter(account=user_account,transaction_type=LOAN)
        print(queryset)
        return queryset
    
    
    
class TransferBalanceView(TransactionCreateMixin,LoginRequiredMixin):
    template_name='transfer_balance.html'
    title = 'Transfer Balance'
    success_url = reverse_lazy('transaction_report')
    form_class = TransferBalanceForm
    
    
    # Backend theke dekha jabe initially
    def get_initial(self):
        initial = {'transaction_type': SEND_MONEY}
        return initial
    
    # if form.is_valid(): 
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        reciever_account_no = form.cleaned_data.get('account_no')
        sender_account = self.request.user.account
        
        reciever_account = UserBankAccount.objects.filter(account_no=reciever_account_no).first()
        
        if reciever_account:
            sender_account.balance -= amount
            sender_account.save(
                update_fields = ['balance']
            )
            reciever_account.balance += amount
            reciever_account.save(
                update_fields = ['balance']
            )
            TransactionModel.objects.create(
                account=sender_account,
                amount=amount,
                balance_after_transaction=sender_account.balance,
                transaction_type=SEND_MONEY,
            )
            TransactionModel.objects.create(
                account=reciever_account,
                amount=amount,
                balance_after_transaction=reciever_account.balance,
                transaction_type=RECIEVED_MONEY,
            )
            messages.success(self.request,f"{amount} $ has been transferred from your account successfully!")
            sendTransactionEmail(self.request.user,amount,"Send Money Message",'send_email.html')
            receiver_user = reciever_account.user
            sendTransactionEmail(receiver_user, amount, "Received Money Message", 'recieved_email.html')
        
        else:
            messages.error(self.request, "Sorry, the given account number is not found!")
            return redirect('transaction_report')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Form is invalid. Please correct the errors.")
        return super().form_invalid(form)
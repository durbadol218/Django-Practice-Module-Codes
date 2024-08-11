from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'userRegistration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        print(user)
        messages.success(self.request,"User account created successfully!")
        return super().form_valid(form) #automatically call korar jonno ai line lekhlam...jodi sobthik thaake tobe automatically kaaj korbe!
    

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        messages.success(self.request,"Account Login successful!")
        return reverse_lazy('homepage')
    
# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('homepage')
class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    

class UserUpdateView(View):
    template_name = 'profile.html'
    
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form}) #automatically call korar jonno ai line lekhlam...jodi sobthik thaake tobe automatically kaaj korbe!
    
def sendEmail(user,subject,template):
    message = render_to_string(template,{
        'user': user,
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,"text/html")
    send_email.send()


class changePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('homepage')
    title = 'Change Password'
    form_class = PasswordChangeForm
    
    
    def form_valid(self, form):
        messages.success(self.request,"Your password has been changed successfully!")
        sendEmail(self.request.user,"Change Password Successfully!",'success_email.html')
        return super().form_valid(form)
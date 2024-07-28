from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import MusicianModel
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
# Create your views here.

def authorRegister(request):
        if request.method == 'POST':
            register_form = forms.RegistrationForm(request.POST) #user kisu akta data pathaise,form ta ar khali nai!
            if register_form.is_valid():
                register_form.save()
                messages.success(request,"Author Account created successfully!")
                return redirect('authorLogin')
        else:
            register_form = forms.RegistrationForm()
        return render(request, 'register.html',{'form':register_form,'type':'Register'})


# Class Based LoginView
class UserLoginView(LoginView):
    template_name = 'register.html'
    
    # success_url = reverse_lazy('authorProfile')
    def get_success_url(self):
        return reverse_lazy('authorProfile')
    
    def form_valid(self, form):
        messages.success(self.request,"Logged in successful!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.danger(self.request,"Logged in information is incorrect!")
        return super().form_invalid(form)
    
    # function a "type" er poriborte amra ekhane aita use korchi!
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
        
# Class Base Logout View
class AuthorLogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect('authorLogin')

#classBased View for add_musician
class AddMusicianView(CreateView):
    model = MusicianModel
    template_name = 'add_musician.html'
    form_class = MusicianForm
    success_url = reverse_lazy('musicians')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = 'add_musician' 
        return context
    

# def edit_musician(request,id):
#     musician = models.MusicianModel.objects.get(pk=id)
#     form = forms.MusicianForm(instance=album)
    
#     if request.method == 'POST':
#         form = forms.MusicianForm(request.POST,instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     form_type = 'updated'
#     return render(request, 'add_musician.html',{'form':form,'form_type':form_type})

# ClassBasedView for EditAlbum
class EditMusicianView(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'add_musician.html'
    success_url = reverse_lazy('musicians')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_type"] = 'updated' 
        return context

class DeleteMusicianView(DeleteView):
    model = MusicianModel
    pk_url_kwarg = 'id'
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('musicians')


# def musician_details(request,id):
#     data = models.MusicianModel.objects.get(pk=id)
#     return render(request,'details_musicians.html',{'musician':data})
class MusicianDetailsView(DetailView):
    model = MusicianModel
    context_object_name = 'musician'
    template_name = 'details_musicians.html'
    pk_url_kwarg = 'id'

class MusiciansView(ListView):
    model = MusicianModel
    template_name = 'musician_lists.html'
    context_object_name = 'musicians'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = 'musicians'
        return context
    

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         profile_form = forms.ChangeUserForm(request.POST,instance=request.user) 
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request,"Profile updated successfully!")
#             return redirect('authorProfile')
#     else:
#         profile_form = forms.ChangeUserForm(instance=request.user)
#     return render(request, 'upgrade_profile.html',{'form':profile_form})


# @login_required
# def authorProfile(request):
#     data = Post.objects.filter(author = request.user)
#     return render(request, 'profile.html',{'data':data})

# @login_required
# def authorLogout(request):
#     logout(request)
#     return redirect('authorLogin')
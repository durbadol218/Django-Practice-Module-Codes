from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserUpdateView, changePasswordView
# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='user_login'),
    path('logout/',UserLogoutView.as_view(), name='user_logout'),
    path('profile/',UserUpdateView.as_view(), name='profile'),
    path('change_password/',changePasswordView.as_view(),name='change_password'),
]
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from musician.views import AuthorLogoutView
urlpatterns = [
    path('add_musician/', views.AddMusicianView.as_view(), name='add_musician'),
    path('authorLogin/',views.UserLoginView.as_view(),name='authorLogin'),
    path('authorLogout/',views.LogoutView.as_view(),name='authorLogout'),
    # path('authorRegister/',views.authorRegister,name='authorRegister'),
    path('', views.MusiciansView.as_view(), name='musicians'),
    # path('edit_musician/<int:id>',views.edit_musician, name='update_musician'),
    path('edit_musician/<int:id>',views.EditMusicianView.as_view(), name='update_musician'),
    # path('delete_musician/<int:id>', views.delete_musician, name='delete_musician'),
    path('delete_musician/<int:id>', views.DeleteMusicianView.as_view(), name='delete_musician'),
    # path('musician_details/<int:id>',views.musician_details,name='musician_details'),
    path('musician_details/<int:id>',views.MusicianDetailsView.as_view(),name='musician_details'),
]
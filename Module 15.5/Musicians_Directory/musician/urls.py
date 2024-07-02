from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('add_musician/', views.add_musician, name='add_musician'),
    path('edit_musician/<int:id>',views.edit_musician, name='update_album'),
    path('delete_musician/<int:id>', views.delete_musician, name='delete_album'),
    path('musician_details/<int:id>',views.musician_details,name='musician_details'),
]
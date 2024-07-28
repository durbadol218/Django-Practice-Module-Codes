from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path('add_album/', views.add_album, name='add_album'),
    path('add_album/', views.AddAlbumView.as_view(), name='add_album'),
    # path('edit_album/<int:id>',views.edit_album, name='update_album'),
    path('edit_album/<int:id>',views.EditAlbumView.as_view(), name='update_album'),
    # path('delete_album/<int:id>', views.delete_album, name='delete_album'),
    path('delete_album/<int:id>', views.DeleteAlbumView.as_view(), name='delete_album'),
]
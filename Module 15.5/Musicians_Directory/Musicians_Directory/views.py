from django.shortcuts import render
from album.models import AlbumModel

def homepage(request):
    data = AlbumModel.objects.all()
    return render(request, 'home.html',{'album_data':data,'current_page':'home'})
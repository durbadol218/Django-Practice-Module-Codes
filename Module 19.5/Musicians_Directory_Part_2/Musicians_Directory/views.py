from django.shortcuts import render
from album.models import AlbumModel
from musician.models import MusicianModel

def homepage(request):
    album_data = AlbumModel.objects.all()
    musicians = MusicianModel.objects.all()
    return render(request, 'home.html',{'album_data':album_data,'musicians':musicians,'current_page':'home'})
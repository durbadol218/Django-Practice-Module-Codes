from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
    else:
        form = forms.AlbumForm()
    return render(request, 'add_album.html',{'form':form})


def edit_album(request,id):
    album = models.AlbumModel.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    form_type = 'updated'
    return render(request, 'add_album.html',{'form':form,'form_type':form_type})

def delete_album(request,id):
    delete_album = models.AlbumModel.objects.get(pk=id)
    delete_album.delete()
    return redirect('homepage')
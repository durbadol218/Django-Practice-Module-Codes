from django.shortcuts import render

# Create your views here.
def add_musician(request):
    return render(request, 'add_musician.html')


from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
    else:
        form = forms.MusicianForm()
    return render(request, 'add_musician.html',{'form':form})


def edit_musician(request,id):
    musician = models.MusicianModel.objects.get(pk=id)
    form = forms.MusicianForm(instance=album)
    
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    form_type = 'updated'
    return render(request, 'add_musician.html',{'form':form,'form_type':form_type})

def delete_musician(request,id):
    delete_mu = models.MusicianModel.objects.get(pk=id)
    delete_mu.delete()
    return redirect('homepage')

def musician_details(request,id):
    data = models.MusicianModel.objects.get(pk=id)
    return render(request,'details_musicians.html',{'musician':data})
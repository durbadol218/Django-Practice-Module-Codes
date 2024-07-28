from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# def add_album(request):
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('homepage')
#     else:
#         form = forms.AlbumForm()
#     return render(request, 'add_album.html',{'form':form})


#classBased View for add_album
class AddAlbumView(CreateView):
    model = AlbumModel
    template_name = 'add_album.html'
    form_class = AlbumForm
    success_url = reverse_lazy('homepage')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = 'add_album' 
        return context
    

# def edit_album(request,id):
#     album = models.AlbumModel.objects.get(pk=id)
#     form = forms.AlbumForm(instance=album)
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST,instance=album)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     form_type = 'updated'
#     return render(request, 'add_album.html',{'form':form,'form_type':form_type})

# ClassBasedView for EditAlbum
class EditAlbumView(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_type"] = 'updated' 
        return context

# def delete_album(request,id):
#     delete_album = models.AlbumModel.objects.get(pk=id)
#     delete_album.delete()
#     return redirect('homepage')


class DeleteAlbumView(DeleteView):
    model = AlbumModel
    pk_url_kwarg = 'id'
    template_name = 'delete_album.html'
    success_url = reverse_lazy('homepage')
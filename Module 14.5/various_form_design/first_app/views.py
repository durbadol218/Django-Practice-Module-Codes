from django.shortcuts import render,redirect
from .forms import ExampleForm

# Create your views here.

def homepage(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("homepage")
    else:
        form = ExampleForm()
    return render(request, "home.html",{"form":form})
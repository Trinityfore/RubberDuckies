from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Duck, Display, Accessories



def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html') 

def duckies_index(request):
    ducks = Duck.objects.all()
    return render(request, 'duckies/index.html', {'ducks' : ducks})

def duckies_detail(request, duck_id):
    duck = Duck.objects.get(id=duck_id)
    return render(request, 'duckies/details.html', {'duck':duck})

class DuckCreate(CreateView): 
    model = Duck
    fields = '__all__'
    success_url = '/cats/'


class DuckUpdate(UpdateView):
    model = Duck
    fields = ('name', 'breed', 'description', 'age')

class DuckDelete(DeleteView):
    model = Duck
    success_url = '/cats/'
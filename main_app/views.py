from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Duck 


def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html') 

def duckies_index(request):
    ducks = Ducks.objects.all()
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
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Duck, Accessories
from .forms import DisplayForm



def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html') 

def duckies_index(request):
    ducks = Duck.objects.all()
    return render(request, 'duckies/index.html', {'ducks' : ducks})

def duckies_detail(request, duck_id):
    duck = Duck.objects.get(id=duck_id)
    display_form = DisplayForm()

    available_accessories = Duck.objects.exclude(id__in = duck.accessories.all().values_list('id'))

    return render(request, 'duckies/details.html', {
        'duck': duck,
        'display_form' : display_form,
        'accessories' : available_accessories,
    })

def add_location(request, duck_id):
    form = DisplayForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.duck_id = duck_id
        new_location.save()
    return redirect ('detail', duck_id=duck_id)

def assoc_access(request, duck_id, accessorie_id):
    Duck.objects.get(id=duck_id).accessories.add(accessorie_id)
    return redirect ('detail', duck_id=duck_id)


class DuckCreate(CreateView): 
    model = Duck
    fields = '__all__'
    success_url = '/duckies/'


class DuckUpdate(UpdateView):
    model = Duck
    fields = ('name', 'year', 'description', 'price')

class DuckDelete(DeleteView):
    model = Duck
    success_url = '/duckies/'

class AccessorieCreate(CreateView):
    model = Accessories
    fields = ('name', 'color')


class AccessorieUpdate(UpdateView):
    model = Accessories
    fields = ('name', 'color')


class AccessorieDelete(DeleteView):
    model = Accessories
    success_url = '/accessories/'


class AccessorieDetail(DetailView):
    model = Accessories
    template_name = 'accessories/detail.html'


class AccessorieList(ListView):
    model = Accessories
    template_name = 'accessories/index.html'
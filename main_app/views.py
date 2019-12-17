from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teddys_index(request):
    return render(
        request, 'teddys/index.html',
        {'teddys': models.Teddy.objects.all()}
    )

def teddys_detail(request, teddy_id):
    return render(request, 'teddys/detail.html', {'teddy': models.Teddy.objects.get(id=teddy_id)})

class TeddyCreate(CreateView):
    model = models.Teddy
    fields = '__all__'

class TeddyUpdate(UpdateView):
    model = models.Teddy
    fields = ['breed','description','birth_year']

class TeddyDelete(DeleteView):
    model = models.Teddy
    success_url = '/teddys/'
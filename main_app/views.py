from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models
from .forms import CleaningForm

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
    teddy = models.Teddy.objects.get(id=teddy_id)
    return render(request, 'teddys/detail.html', {
        'teddy': teddy,
        'cleaning_form': CleaningForm
    })

class TeddyCreate(CreateView):
    model = models.Teddy
    fields = '__all__'

class TeddyUpdate(UpdateView):
    model = models.Teddy
    fields = ['breed','description','birth_year']

class TeddyDelete(DeleteView):
    model = models.Teddy
    success_url = '/teddys/'

def add_cleaning(request, teddy_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.teddy_id = teddy_id
        new_cleaning.save()
    return redirect('detail', teddy_id=teddy_id)

class ClothesList(ListView):
    model = models.Cloth
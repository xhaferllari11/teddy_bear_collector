from django.shortcuts import render
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
    print(f'ok {models.Teddy.objects.filter(id=teddy_id)}')
    return render(request, 'teddys/detail.html', {'teddy': models.Teddy.objects.get(id=teddy_id)})



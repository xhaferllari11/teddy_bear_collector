from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import uuid
import boto3
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
    clothes_teddy_doesnt_have = models.Cloth.objects.exclude(id__in = teddy.clothes.all().values_list('id'))

    return render(request, 'teddys/detail.html', {
        'teddy': teddy,
        'cleaning_form': CleaningForm,
        'clothes': clothes_teddy_doesnt_have
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

class ClothesDetail(DetailView):
    model = models.Cloth

class ClothesUpdate(UpdateView):
    model = models.Cloth
    fields = ['item','color']

class ClothesDelete(DeleteView):
    model = models.Cloth
    success_url = '/clothes/'

class ClothesCreate(CreateView):
    model = models.Cloth
    fields = '__all__'

def assoc_cloth(request, teddy_id, cloth_id):
    teddy = models.Teddy.objects.get(id=teddy_id)
    teddy.clothes.add(cloth_id)
    return redirect(teddy)

def add_photo(request, teddy_id):
    S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
    BUCKET = 'teddycollector-alban'
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to teddy_id or cat (if you have a cat object)
            photo = models.Photo(url=url, teddy_id=teddy_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', teddy_id=teddy_id)
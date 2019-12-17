from django.db import models
from django.urls import reverse

# Create your models here.

class Teddy(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    birth_year = models.IntegerField()

    def __str__(self):
        return f'name: {self.name} id: {self.id}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'teddy_id': self.id})
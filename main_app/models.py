from django.db import models
from django.urls import reverse

# Create your models here.

DIRTINESS = (
    ('D', 'Diry'),
    ('S', 'Somewhat Dirty'),
    ('C', 'Clean')
)

class Cloth(models.Model):
    item = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'item: {self.item}'

    def get_absolute_url(self):
        return reverse('clothes_detail', kwargs={'pk': self.id})


class Teddy(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    birth_year = models.IntegerField()
    clothes = models.ManyToManyField(Cloth)

    def __str__(self):
        return f'name: {self.name} id: {self.id}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'teddy_id': self.id})

class Cleaning(models.Model):
    date = models.DateField()
    dirt = models.CharField(
        max_length=1,
        choices=DIRTINESS,
        default=DIRTINESS[0][0]
    )
    teddy = models.ForeignKey(Teddy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_dirt_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


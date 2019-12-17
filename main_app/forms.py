from django.forms import ModelForm
from .models import Cleaning

class CleaningForm(ModelForm):
    class Meta:
        model = Cleaning
        fields = ['date','dirt']
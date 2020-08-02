# forms.py 
from django import forms 
from .models import *
  
class CropForm(forms.ModelForm): 
    class Meta: 
        model = Crop
        fields = ['name', 'image'] 
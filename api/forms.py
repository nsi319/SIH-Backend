# forms.py 
from django import forms 
from .models import *
  
class CropForm(forms.ModelForm): 
    class Meta: 
        model = Crop
        fields = ['name', 'image'] 

class CropForm2(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['year','month','rainfall','mandi']
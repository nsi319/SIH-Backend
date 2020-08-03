from django.db import models

# Create your models here.
class Crop(models.Model): 
    name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/') 
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    rainfall = models.IntegerField(default=0)
    mandi = models.CharField(max_length=100,default='Indore')
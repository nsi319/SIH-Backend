from django.db import models

# Create your models here.
class Crop(models.Model): 
    name = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='images/') 
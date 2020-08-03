from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
    path('image_upload',crop_image, name = 'image_upload'),
    path('get_price',get_price,name='get_price') 
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
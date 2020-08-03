from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from utils.modelForCropHealthPrediction import test_data
from utils.modelforcrop import prediction
from pathlib import Path
import os
import shutil


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
image_dir = PROJECT_PATH + "/media/"
  
# Create your views here. 
@require_http_methods(['POST'])
@csrf_exempt
def crop_image(request): 
    data = {}
    if request.method == 'POST': 
        form = CropForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            print(form.cleaned_data['name'])
            print(form.cleaned_data['image'])
            predict = test_data()
            data['response']='success'
            data['predict'] = predict[0]

            shutil.rmtree(image_dir)

            return JsonResponse(data)
    else: 
        form = CropForm() 
    image_dir.rmdir()
    data['response']='failure'
    return JsonResponse(data)
     
@require_http_methods(['POST'])
@csrf_exempt
def get_price(request): 
    data = {}
    if request.method == 'POST': 
        form = CropForm2(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
            input_data = {'year' : form.cleaned_data['year'],'month' : form.cleaned_data['month'],'rainfall' : form.cleaned_data['rainfall'],'mandi' : form.cleaned_data['mandi']}
            predict = prediction(input_data)
            data['response']='success'
            data['predict'] = str(predict[0][0])
            return JsonResponse(data)
    else: 
        form = CropForm2() 
    data['response']='failure'
    return JsonResponse(data)
     
  
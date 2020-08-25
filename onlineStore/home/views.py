from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def home(request):
    prod1 = product()
    prod1.name = 'chair'
    prod1.price = 400
    prod1.img = "chair.jpeg"

    
    prod2 = product()
    prod2.name = 'sofa'
    prod2.price = 8000
    prod2.img = "sofa.jpeg"
   
    prod3 = product()
    prod3.name = 'bed'
    prod3.price = 4000
    prod3.img = "bed.jpeg"

    prod4 = product()
    prod4.name = 'wardrobe'
    prod4.price = 2500
    prod4.img = "wardrobe.jpeg"

 

   
    products = [prod1,prod2,prod3,prod4]

    return render(request,'index.html',{'products': products})
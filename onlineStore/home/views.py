from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def home(request):
    prod1 = product()
    prod1.name = 'chair'
    prod1.price = 400
    return render(request,'index.html',{'prod1': prod1})
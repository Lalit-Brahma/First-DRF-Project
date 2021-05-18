from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import wpn, clt, fod

def home(request):
    return render(request, 'titan/home.html')
        
    
def shopping(request):
    return render(request, 'titan/shop.html')

def weapons(request):
    context1 = {
        'wpns' : wpn.objects.all()
    }
    return render(request, 'titan/weapons.html', context1)

def clothes(request):
    context2 = {
        'clts' : clt.objects.all()
    }
    return render(request, 'titan/clothes.html', context2)

def food(request):
    context3 = {
        'fods' : fod.objects.all()
    }
    return render(request, 'titan/food.html', context3)

@login_required
def transaction(request):
    return render(request, 'titan/transaction.html')

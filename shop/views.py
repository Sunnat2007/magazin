from django.shortcuts import render
from .models import *

# Create your views here.


def base(request):
    return render(request, "base.html", {})



def iphones(request):
    iphone = Iphone.objects.all()
    return render(request, "iphone.html", {
        'iphones' :iphone
        })
def iphone(request, slug):
    iphone = Iphone.objects.get(slug=slug)
    return render(request, "product.html", {
        'iphone': iphone,
        })



def nokias(request):
    nokia = Nokia.objects.all()
    return render(request, "nokia.html", {
        'nokias' :nokia
        })
def nokia(request, slug):
    nokia = Nokia.objects.get(slug=slug)
    return render(request, "product1.html", {
        'nokia': nokia,
        })



def redmis(request):
    redmi = Redmi.objects.all()
    return render(request, "redmi.html", {
        'redmis' :redmi
        })
def redmi(request, slug):
    redmi = Redmi.objects.get(slug=slug)
    return render(request, "product2.html", {
        'redmi': redmi,
        })


def others(request):
    other = Others.objects.all()
    return render(request, "others.html", {
        'others' :other
        })
def other(request, slug):
    other = Others.objects.get(slug=slug)
    return render(request, "product3.html", {
        'other': other,
        })


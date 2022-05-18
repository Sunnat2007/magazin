from django.shortcuts import render
from .models import *

# Create your views here.


def product(request):
    product = Product.objects.all()
    return render(request, "product.html", {
        'products' :product
        })
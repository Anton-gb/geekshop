from django.shortcuts import render
import json

from mainapp.models import Product, Category


def index(requests):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(requests, 'mainapp/index.html', context)


def products(requests):

    context = {
        'links_menu': Category.objects.all()
    }

    return render(requests, 'mainapp/products.html', context)


def products_list(requests, pk):
    print(pk)
    context = {
        'links_menu': Category.objects.all()
    }
    return render(requests, 'mainapp/products.html', context)


def contact(requests):
    return render(requests, 'mainapp/contact.html')

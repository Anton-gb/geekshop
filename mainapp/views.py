from django.shortcuts import render


def index(requests):
    return render(requests, 'mainapp/index.html')


def products(requests):
    return render(requests, 'mainapp/products.html')


def contact(requests):
    return render(requests, 'mainapp/contact.html')

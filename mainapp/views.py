from django.shortcuts import render
import json


def index(requests):
    return render(requests, 'mainapp/index.html')


def products(requests):
    with open('mainapp/templates/mainapp/data.json', 'r', encoding='utf-8') as file:
        links_menu = json.load(file)

    context = {
        'links_menu': links_menu
    }

    return render(requests, 'mainapp/products.html', context)


def contact(requests):
    return render(requests, 'mainapp/contact.html')

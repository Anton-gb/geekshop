from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import products, product

app_name = 'products'
# app_name = MainappConfig.name

urlpatterns = [
    path('', products, name='products_hot_product'),
    path('<int:pk>/', products, name='product_list'),
    path('product/<int:pk>/', product, name='product_item'),
]

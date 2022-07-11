from django.urls import path

from basketapp.views import basket_add, basket_list, basket_remove

app_name = 'basket'

urlpatterns = [
    path('', basket_list, name='list'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
]

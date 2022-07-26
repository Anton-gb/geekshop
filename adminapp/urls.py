from django.urls import path
from adminapp import views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UserListView.as_view(), name='user_read'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.CategoryReadView.as_view(), name='category_read'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('categories/products/read/<int:pk>/', adminapp.CategoryDetailView.as_view(), name='products_read'),
    path('product/create/<int:pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('product/detail/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_detail'),
]

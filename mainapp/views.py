from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import Product, Category
from mainapp.services import get_basket, get_hot_product, get_same_products
from django.views.generic import TemplateView


def index(request):
    context = {
        'products': Product.objects.all()[:4],
    }
    return render(request, 'mainapp/index.html', context)


# class IndexView(TemplateView):
#     template_name = 'mainapp/index.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['products'] = Product.objects.all()[:4]
#         return context_data


def products(request, pk=None):
    links_menu = Category.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'все', 'pk': 0}
        else:
            products_list = Product.objects.filter(category_id=pk)
            category_item = get_object_or_404(Category, pk=pk)

        page = request.GET.get('page')
        paginator = Paginator(products_list, 2)
        try:
            paginated_products = paginator.page(page)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        except EmptyPage:
            paginated_products = paginator.page(paginator.num_pages)

        context = {
            'links_menu': links_menu,
            'products': paginated_products,
            'category': category_item,
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    context = {
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'product': product_item,
        'links_menu': Category.objects.all(),
    }
    return render(request, 'mainapp/product.html', context)


def contact(request):
    context = {
        
    }
    return render(request, 'mainapp/contact.html', context)

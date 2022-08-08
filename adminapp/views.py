from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminEditForm, ProductEditForm, CategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


class AccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     return None


class UserCreateView(AccessMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserRegisterForm
    success_url = reverse_lazy('adminapp:user_read')


# @user_passes_test(lambda u: u.is_superuser)
# def user_read(request):
#     context = {
#         'objects': ShopUser.objects.all().order_by('-is_active', 'is_superuser')
#     }
#     return render(request, 'adminapp/user_list.html', context)


class UserListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/user_list.html'
    paginate_by = 5
    extra_context = {
        'title': 'Список пользователей'
    }
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     context_data['user_hello_text'] = self.request.user.get_full_name()
    #     return context_data


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = UserAdminEditForm(request.POST, request.FILES, instance=user_item)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[pk]))
#     else:
#         edit_form = UserAdminEditForm(instance=user_item)
#
#     context = {
#         'form': edit_form
#     }
#     return render(request, 'adminapp/user_form.html', context)


class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = UserAdminEditForm
    success_url = reverse_lazy('adminapp:user_read')

    # def get_success_url(self):
    #     return reverse('adminapp:user_update', args=[self.kwargs.get('pk')])


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_item.is_active = False
#         user_item.save()
#         return HttpResponseRedirect(reverse('adminapp:user_read'))
#     context = {
#         'objects': user_item
#     }
#     return render(request, 'adminapp/user_delete_confirm.html', context)


class UserDeleteView(AccessMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete_confirm.html'
    success_url = reverse_lazy('adminapp:user_read')

    def form_valid(self, form):
        user = self.get_object()
        user.is_active = False
        user.save()
        return HttpResponseRedirect(self.success_url)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     return None


class CategoryCreateView(AccessMixin, CreateView):
    model = Category
    # form_class = CategoryEditForm
    fields = ('name', 'description',)
    template_name = 'adminapp/category_form.html'
    success_url = reverse_lazy('adminapp:category_read')


# @user_passes_test(lambda u: u.is_superuser)
# def category_read(request):
#     context = {
#         'objects_list': Category.objects.all().order_by('-is_active')
#     }
#     return render(request, 'adminapp/category_list.html', context)


class CategoryReadView(AccessMixin, ListView):
    model = Category
    template_name = 'adminapp/category_list.html'
    extra_context = {
        'title': 'Список категорий'
    }


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request):
#     return None


class CategoryUpdateView(AccessMixin, UpdateView):
    model = Category
    template_name = 'adminapp/category_form.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:category_read')

    # def form_valid(self, form):
    #     self.object = self.get_object()
    #     if self.object.is_active:
    #         for product in self.object.product_set.all():
    #             product.is_active = True
    #             product.save()
    #     return HttpResponseRedirect(self.success_url)


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request):
#     return None


class CategoryDeleteView(AccessMixin, DeleteView):
    model = Category
    template_name = 'adminapp/category_delete_confirm.html'
    success_url = reverse_lazy('adminapp:category_read')

    def form_valid(self, form):
        category = self.get_object()
        category.is_active = False
        category.save()
        # for product in self.object.product_set.all():
        #     product.is_active = False
        #     product.save()
        return HttpResponseRedirect(self.success_url)


# @user_passes_test(lambda u: u.is_superuser)
# def products_read(request, pk):
#     category_item = get_object_or_404(Category, pk=pk)
#     products_list = Product.objects.filter(category_id=pk)
#     context = {
#         'objects_list': products_list,
#         'category': category_item,
#     }
#
#     return render(request, 'adminapp/products_list.html', context)


# class ProductListView(AccessMixin, ListView):
#     model = Product
#     template_name = 'adminapp/products_list.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#         context_data['category'] = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#         return context_data
#
#     def get_queryset(self):
#         return super().get_queryset().filter(category_id=self.kwargs.get('pk'))


class CategoryDetailView(AccessMixin, DetailView):
    model = Category
    template_name = 'adminapp/products_list.html'


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     # category_item = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_item = product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products_read', args=[product_item.category_id]))
#     else:
#         product_form = ProductEditForm(initial={'category': pk})
#
#     context = {
#         'form': product_form,
#     }
#     return render(request, 'adminapp/product_form.html', context)


class ProductCreateView(AccessMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        category_pk = self.request.POST.get('category')
        return reverse('adminapp:products_read', args=[category_pk])

    def get_initial(self):
        initial = super().get_initial()
        initial['category'] = self.kwargs.get('pk')
        return initial


# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request):
#     return None


class ProductUpdateView(AccessMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    fields = '__all__'

    def get_success_url(self):
        category_pk = self.get_object().category_id
        return reverse('adminapp:products_read', args=[category_pk])


# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request):
#     return None


class ProductDeleteView(AccessMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete_confirm.html'

    def get_success_url(self):
        category_pk = self.get_object().category_id
        return reverse('adminapp:products_read', args=[category_pk])

    def form_valid(self, form):
        url = self.get_success_url()
        # if 'delete_product' in form.data:
        #     self.object = self.get_object()
        #     self.object.delete()
        # elif 'really_delete_product' in form.data:
        #     self.object = self.get_object()
        #     self.object.really_delete()
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(url)


# @user_passes_test(lambda u: u.is_superuser)
# def product_detail(request):
#     return None


class ProductDetailView(AccessMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_info.html'

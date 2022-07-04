from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(requests):
    login_form = ShopUserLoginForm(data=requests.POST)
    if requests.method == 'POST' and login_form.is_valid():
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(requests, user)
            return HttpResponseRedirect(reverse('index'))
    context = {
        'form': login_form,
        'title': 'Вход в систему'
    }
    return render(requests, 'authapp/login.html', context)


def logout(requests):
    auth.logout(requests)
    return HttpResponseRedirect(reverse('index'))


def register(requests):
    if requests.method == 'POST':
        register_form = ShopUserRegisterForm(requests.POST, requests.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'form': register_form,
        'title': 'Регистрация'
    }
    return render(requests, 'authapp/register.html', context)


def edit(requests):
    if requests.method == 'POST':
        edit_form = ShopUserEditForm(requests.POST, requests.FILES, instance=requests.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))

    else:
        edit_form = ShopUserEditForm(instance=requests.user)

    context = {
        'form': edit_form,
        'title': 'Редактирование профиля'
    }
    return render(requests, 'authapp/edit.html', context)

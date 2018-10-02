from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import *
from .menu import *
from client import *


def main(request):
    title = 'Мессенжер-Главная'
    content = {
        'title': title,
        'links_menu': links_menu,
        'status_server': check_server(),
        'wr_mes': write_message,
        'rd_mes': read_message,
    }
    return render(request, 'mainapp/index.html', content)


def check_server(username = 'suite', password = 'TsEUsItTe'):
    client = Client({'login': username, 'password': password})
    while True:
        status = 'disconnect'
        if client.connect_server():
            status = 'connect'

        # else:
        #     status = 'disconnect'

        return status


def write_message(request):
    pass


def read_message(request):
    pass


def login(request):
    title = 'Мессенжер-Вход'
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    content = {
        'title': title,
        'login_form': login_form,
    }
    return render(request, 'mainapp/login.html', content)


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('main'))


def edit(request):
    title = 'Мессенжер-Редактирование'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('edit'))

    else:
        edit_form = UserEditForm(instance=request.user)

    content = {
        'title': title,
        'edit_form': edit_form
    }

    return render(request, 'mainapp/edit.html', content)


def register(request):
    title = 'Мессенжер-Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('login'))

    else:
        register_form = UserRegisterForm()

    content ={
        'title': title,
        'register_form': register_form
    }

    return render(request, 'mainapp/register.html', content)
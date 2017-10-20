# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_user, logout as logout_user
from django.http import HttpResponseRedirect
from .models import User
from .forms import Cadastro, Login

# Create your views here.
def cadastro(request):
    return render(request, 'usuario/cadastro.html', {}, content_type='text/html')


def cadastrado(request):
    return render(request, 'usuario/cadastrado.html', {}, content_type='text/html')


def login(request):
    return render(request, 'usuario/login.html', {}, content_type='text/html')

def logout(request):
    logout_user(request)
    return HttpResponseRedirect('/')


def cadastrar(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'], form.cleaned_data['user_type'])
            return HttpResponseRedirect('/usuario/cadastrado/')

    else:
        form = Cadastro()

    return render(request, 'usuario/cadastro.html', {'form': form})


def logar(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            usuario = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if usuario is not None:
                auth_user(request, usuario)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'usuario/login.html', {'mensagem': "E-mail não cadastrado ou senha incorreta."})


def recuperar_senha(request):
    return render(request, 'usuario/recuperar-senha.html', {}, content_type='text/html')
# encoding: utf-8

from django import forms

class Cadastro(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100)
    username = forms.CharField(label='Usuário', max_length=100)
    password = forms.CharField(label='Senha', max_length=100)
    user_type = forms.CharField(label='Tipo', max_length=100)


class Login(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100)
    password = forms.CharField(label='Senha', max_length=100)
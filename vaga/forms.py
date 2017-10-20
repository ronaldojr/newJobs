# encoding: utf-8

from django import forms

class CadastroVaga(forms.Form):
    nome = forms.CharField(label='Nome da vaga', max_length=100)
    faixaSalarialMin = forms.DecimalField(label='Faixa Salárial (min)')
    faixaSalarialMax = forms.DecimalField(label='Faixa Salárial (min)')
    experiencia = forms.IntegerField(label='Experiência (anos)')
    escolaridade = forms.CharField(label='Escolaridade', max_length=100)
    distancia = forms.IntegerField(label='Distância (Kms)')


class CadastroCandidatura(forms.Form):
    vaga = forms.IntegerField()
    pretensao = forms.DecimalField(label='Pretensão Salárial')
    experiencia = forms.IntegerField(label='Experiência (anos)')
    escolaridade = forms.CharField(label='Escolaridade', max_length=19)
    distancia = forms.IntegerField(label='Distância (Kms)')
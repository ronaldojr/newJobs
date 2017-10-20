# -*- coding: utf-8 -*-

from django.shortcuts import render
from vaga.models import Vaga

def index(request):
    try:
        #exibe apenas as últimas quatro vagas cadastradas
        vagas = Vaga.objects.all()[:4]
    except:
        vagas = []
    return render(request, 'core/base.html', {'vagas': vagas}, content_type='text/html')



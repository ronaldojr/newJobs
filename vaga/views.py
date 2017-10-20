# -*- coding: utf-8 -*-

from .models import Vaga, Candidatura
from .forms import CadastroVaga, CadastroCandidatura
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist



def pesquisar(request):
    """
    responsável por carregar o resultado da página de pesquisa
    """
    if request.method == 'POST':
         termo = request.POST['pesquisar']
    else:
         termo = request.GET.get('termo')
    try:
        lista_vagas = Vaga.objects.filter(nome__contains=termo)
        paginator = Paginator(lista_vagas, 8)
        page = request.GET.get('page')
        try:
            vagas = paginator.page(page)
        except PageNotAnInteger:
            vagas = paginator.page(1)
        except EmptyPage:
            vagas = paginator.page(paginator.num_pages)
        return render(request, 'vaga/pesquisar.html', {'vagas':vagas, 'termo': termo}, content_type='text/html')
    except:
        return render(request, 'vaga/erro-pesquisar-vagas.html', {}, content_type='text/html')


def listar_vagas(request):
    """
    responsável por exibir a lista de vagas 
    """
    try:
        lista_vagas = Vaga.objects.all()
        paginator = Paginator(lista_vagas, 8)
        page = request.GET.get('page')
        try:
            vagas = paginator.page(page)
        except PageNotAnInteger:
            vagas = paginator.page(1)
        except EmptyPage:
            vagas = paginator.page(paginator.num_pages)

    except:
        vagas = []

    return render(request, 'vaga/listar-vagas.html', {'vagas':vagas}, content_type='text/html')


def gerenciar_vagas(request):
    """
    exibe páginas de genrenciamento de vagas do usuário logado
    """
    try:
        vagas = Vaga.objects.filter(empresa=request.user)
    except ObjectDoesNotExist:
        vagas = []
    
    return render(request, 'vaga/gerenciar-vagas.html', {'vagas': vagas}, content_type='text/html')


def cadastrar_vaga(request):
    """
    recebe dados de uma nova vaga para ser cadastrada e insere no banco 
    apos validar dados do formulario
    """
    try:
        vagas = Vaga.objects.filter(empresa=request.user)
    except ObjectDoesNotExist:
        vagas = []

    if request.method == 'POST':
        form = CadastroVaga(request.POST)
        if form.is_valid():
            vaga = Vaga(empresa=request.user, 
                        nome=form.cleaned_data['nome'], 
                        faixaSalarialMin=float(form.cleaned_data['faixaSalarialMin']), 
                        faixaSalarialMax=float(form.cleaned_data['faixaSalarialMax']), 
                        experiencia=form.cleaned_data['experiencia'], 
                        escolaridade=form.cleaned_data['escolaridade'], 
                        distancia=form.cleaned_data['distancia'])
            vaga.save()
            return render(request, 'vaga/gerenciar-vagas.html', {'vagas': vagas}, content_type='text/html')

    else:
        form = CadastroVaga()

    return render(request, 'vaga/gerenciar-vagas.html', {'form': form, 'vagas': vagas}, content_type='text/html')


def relatorios(request):
    """
    responsável por exibir relatorios
    """
    lista_vagas = []
    try:
        vagas = Vaga.objects.filter(empresa=request.user)
        for vaga in vagas:
            candidaturas = Candidatura.objects.filter(vaga=vaga)
            candidaturas_classificadas = classificar_candidaturas(vaga, candidaturas)
            lista_vagas.append({'vaga': vaga, 
                                'candidaturas_validas':candidaturas_classificadas['candidaturas_validas'], 
                                'total_validas':candidaturas_classificadas['total_validas'], 
                                'total_invalidas': candidaturas_classificadas['total_invalidas']})
    except:
        return render(request, 'vaga/relatorios.html', {'erro': "Erro ao gerar relatório"}, content_type='text/html')

    return render(request, 'vaga/relatorios.html', {'vagas': lista_vagas}, content_type='text/html')


def classificar_candidaturas(vaga, candidaturas):
    """
    Confere dados da vaga com dados das candidaturas
    """
    lista_validas = []
    conta_invalidas = 0

    peso_escolaridade = {'MEDIO': 1, 
                         'SUPERIOR_INC': 2, 
                         'SUPERIOR_COM': 3,
                         'MESTRADO': 4,
                         'DOUTORADO': 5}

    for candidatura in candidaturas:
        if candidatura.pretensao < vaga.faixaSalarialMin and candidatura.pretensao > vaga.faixaSalarialMax:
            conta_invalidas = conta_invalidas + 1
            continue

        if candidatura.experiencia < vaga.experiencia:
            conta_invalidas = conta_invalidas +1
            continue

        if peso_escolaridade[candidatura.escolaridade] < peso_escolaridade[vaga.escolaridade]:
            conta_invalidas = conta_invalidas +1
            continue

        if candidatura.distancia > vaga.distancia:
            conta_invalidas = conta_invalidas +1
            continue

        lista_validas.append(candidatura)

    return {'candidaturas_validas': lista_validas, 
            'total_validas': len(lista_validas), 
            'total_invalidas': conta_invalidas}


def candidaturas(request):
    """
    responsável por exibir as candidaturas do candidato logado
    """
    try:
        candidaturas = Candidatura.objects.filter(candidato=request.user)
    except:
        candidaturas = []

    return render(request, 'vaga/candidaturas.html', {'candidaturas': candidaturas}, content_type='text/html')



def candidatar(request, vaga_id):
    """
    responsável por exibir formulário para usuário se candidatar a vaga
    """
    if not request.user.is_authenticated():
        return render(request, 'vaga/erro-logar-sistema.html', {}, content_type='text/html')

    try:
        vaga = Vaga.objects.get(id=vaga_id)
        candidatura = Candidatura.objects.filter(vaga=vaga, candidato=request.user)
        if candidatura:
            return render(request, 'vaga/erro-candidatura-ja-efetuada.html', {}, content_type='text/html')
    except:
        return render(request, 'vaga/erro-vaga-nao-encontrada.html', {}, content_type='text/html')

    return render(request, 'vaga/candidatar.html', {'vaga':vaga}, content_type='text/html')



def finalizar_candidatura(request):
    """
    responsável por vincular dados da candidatura do usuário a vaga selecionada
    """
    if request.method == 'POST':
        form = CadastroCandidatura(request.POST)
        vaga = get_vaga_from_id(request.POST['vaga'])
        if form.is_valid():
            candidato = request.user
            pretensao = form.cleaned_data['pretensao']
            escolaridade = form.cleaned_data['escolaridade']
            experiencia = form.cleaned_data['experiencia']
            distancia = form.cleaned_data['distancia']
            candidatura = Candidatura(vaga=vaga, 
                                      candidato=candidato, 
                                      pretensao=pretensao, 
                                      experiencia=experiencia, 
                                      escolaridade=escolaridade, 
                                      distancia=distancia)
            candidatura.save()
            return HttpResponseRedirect('/vaga/candidaturas/')
    else:
        form = CadastroCandidatura()

    return render(request, 'vaga/candidatar.html', {'vaga':vaga, 'form': form}, content_type='text/html')
            


def get_vaga_from_id(id):
    """
    função que retorna vaga de acordo com id passado por parametro
    """
    try:
        vaga = Vaga.objects.get(id=id)
        return vaga
    except:
        return render(request, 'vaga/erro-vaga-nao-encontrada.html', {}, content_type='text/html')

    

#requisições AJAX


def editar_vaga(request):
    """
    recebe dados da vaga via ajax (POST) para atualização
    """
    if request.is_ajax():
        return JsonResponse({'response': 'problemas com envio de dados'})

    try:
        vaga = Vaga.objects.get(id=request.POST['id'])
        vaga.nome = request.POST['nome']
        vaga.faixaSalarialMin = float(request.POST['faixaSalarialMin'])
        vaga.faixaSalarialMax = float(request.POST['faixaSalarialMax'])
        vaga.experiencia = request.POST['experiencia']
        vaga.escolaridade = request.POST['escolaridade']
        vaga.distancia = request.POST['distancia']
        vaga.save()
        return JsonResponse({'response': 'ok'})
    except:
        return JsonResponse({'response': 'erro ao atualizar vaga'})


def excluir_vaga(request):
    """
    recebe id da vaga via ajax (POST) para exclusão
    """
    if request.is_ajax():
        return JsonResponse({'response': 'problemas com envio de dados'})

    try:
        vaga = Vaga.objects.get(id=request.POST['id']).delete()
        return JsonResponse({'response': 'ok'})
    except:
        return JsonResponse({'response': 'erro ao apagar vaga'})
        

def editar_candidatura(request):
    """
    recebe o status da candidatura via ajax (POST) para atualização
    """
    if not request.is_ajax():
        return JsonResponse({'response': 'problemas com envio de dados'})
    
    try:
        candidatura = Candidatura.objects.get(id=request.POST['id'])
        candidatura.status = request.POST['status']
        candidatura.save()
        return JsonResponse({'response': 'ok'})
    except:
        return JsonResponse({'response': 'erro ao atualizar candidatura'})
        


def excluir_candidatura(request):
    """
    recebe id da candidatura via ajax (POST) para exclusão
    """
    if not request.is_ajax():
        return JsonResponse({'response': 'problemas com envio de dados'})

    try:
        candidatura = Candidatura.objects.get(id=request.POST['id']).delete()
        return JsonResponse({'response': 'ok'})
    except:
        return JsonResponse({'response': 'erro ao apagar candidatura'})
    
        


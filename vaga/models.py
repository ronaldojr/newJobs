# -*- coding: utf-8 -*-

from django.db import models
from usuario.models import User


ESCOLARIDADE_OPCOES = (
    ('MEDIO', "Ensino Medio"),
    ('SUPERIOR_INC', "Superior Incompleto"),
    ('SUPERIOR_COM', "Superior Completo"),
    ('MESTRADO', "Mestrado"),
    ('DOUTORADO', "Doutorado"),
)

STATUS_OPCOES = (
    ('A', "Aguardando avaliação"),
    ('B', "Em avaliação"),
    ('C', "Aprovado"),
    ('D', "Reprovado"),
)


class Vaga(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120, verbose_name='Nome da Vaga')
    faixaSalarialMin = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Faixa Salarial mínima")
    faixaSalarialMax = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Faixa Salarial máxima")
    experiencia = models.IntegerField(verbose_name="Anos de Experiência")
    escolaridade = models.CharField(max_length=19, choices=ESCOLARIDADE_OPCOES, default='MEDIO')
    distancia = models.IntegerField(verbose_name="Distância em Kms")


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    pretensao = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Faixa Salarial")
    experiencia = models.IntegerField(verbose_name="Anos de Experiência")
    escolaridade = models.CharField(max_length=19, choices=ESCOLARIDADE_OPCOES, default='MEDIO')
    distancia = models.IntegerField(verbose_name="Distância em Kms")
    status = models.CharField(max_length=20, choices=STATUS_OPCOES, default='A')
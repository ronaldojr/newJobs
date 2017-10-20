# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pretensao', models.DecimalField(verbose_name=b'Faixa Salarial', max_digits=20, decimal_places=2)),
                ('experiencia', models.IntegerField(verbose_name=b'Anos de Experi\xc3\xaancia')),
                ('escolaridade', models.CharField(default=b'MEDIO', max_length=19, choices=[(b'MEDIO', b'Ensino Medio'), (b'SUPERIOR_INC', b'Superior Incompleto'), (b'SUPERIOR_COM', b'Superior Completo'), (b'MESTRADO', b'Mestrado'), (b'DOUTORADO', b'Doutorado')])),
                ('distancia', models.IntegerField(verbose_name=b'Dist\xc3\xa2ncia em Kms')),
                ('status', models.CharField(default=b'A', max_length=20, choices=[(b'A', b'Aguardando avalia\xc3\xa7\xc3\xa3o'), (b'B', b'Em avalia\xc3\xa7\xc3\xa3o'), (b'C', b'Aprovado'), (b'D', b'Reprovado')])),
                ('candidato', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=120, verbose_name=b'Nome da Vaga')),
                ('faixaSalarialMin', models.DecimalField(verbose_name=b'Faixa Salarial m\xc3\xadnima', max_digits=20, decimal_places=2)),
                ('faixaSalarialMax', models.DecimalField(verbose_name=b'Faixa Salarial m\xc3\xa1xima', max_digits=20, decimal_places=2)),
                ('experiencia', models.IntegerField(verbose_name=b'Anos de Experi\xc3\xaancia')),
                ('escolaridade', models.CharField(default=b'MEDIO', max_length=19, choices=[(b'MEDIO', b'Ensino Medio'), (b'SUPERIOR_INC', b'Superior Incompleto'), (b'SUPERIOR_COM', b'Superior Completo'), (b'MESTRADO', b'Mestrado'), (b'DOUTORADO', b'Doutorado')])),
                ('distancia', models.IntegerField(verbose_name=b'Dist\xc3\xa2ncia em Kms')),
                ('empresa', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidatura',
            name='vaga',
            field=models.ForeignKey(to='vaga.Vaga'),
        ),
    ]

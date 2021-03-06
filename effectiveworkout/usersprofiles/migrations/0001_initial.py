# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monthlyplans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=50, verbose_name='Sobrenome')),
                ('emailatleta', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('datainicio', models.DateField(verbose_name='Data de inicio')),
                ('datanascimento', models.DateField(verbose_name='Data de nascimento')),
                ('idade', models.IntegerField(blank=True, verbose_name='Idade')),
                ('cc', models.CharField(max_length=12, verbose_name='Cartão do Cidadão')),
                ('nif', models.IntegerField(verbose_name='Número de Identifacação Fiscal')),
                ('telefone', models.CharField(max_length=9, verbose_name='Nº Telefone')),
                ('telefone2', models.CharField(blank=True, max_length=9, verbose_name='Nº Telefone urgência')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('ativo', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Ativo')),
                ('planomensalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthlyplans.PlanoMensalidade', verbose_name='Planos e mensalidade')),
            ],
            options={
                'verbose_name': 'Inscrição Atleta',
                'verbose_name_plural': 'Inscrições Atletas',
                'ordering': ('nome',),
            },
        ),
    ]

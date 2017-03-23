# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-06 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Артикул')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('link', models.URLField(max_length=128, unique=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=32, unique=True, verbose_name='Артикул')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Артикул')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='static/pics/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spigen.Category', verbose_name='Категория')),
            ],
        ),
    ]
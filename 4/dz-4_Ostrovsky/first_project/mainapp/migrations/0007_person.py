# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20170123_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='ФИО')),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
        ),
    ]

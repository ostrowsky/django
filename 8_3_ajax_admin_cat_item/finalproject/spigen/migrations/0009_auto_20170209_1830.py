# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spigen', '0008_auto_20170209_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Наименование'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spigen', '0006_auto_20170209_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='pics/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preview',
            field=models.ImageField(blank=True, upload_to='pics/', verbose_name='Превью'),
        ),
    ]

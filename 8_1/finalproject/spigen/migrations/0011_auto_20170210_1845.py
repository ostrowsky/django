# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spigen', '0010_auto_20170210_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='media/pics/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preview',
            field=models.ImageField(upload_to='media/pics/previews', verbose_name='Превью'),
        ),
    ]
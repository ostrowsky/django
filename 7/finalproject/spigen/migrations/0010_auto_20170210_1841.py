# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spigen', '0009_auto_20170209_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/pics/', verbose_name='Изображение'),
        ),
    ]

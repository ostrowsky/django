# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_work_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.TextField(blank='True', verbose_name='Ссылка'),
        ),
    ]

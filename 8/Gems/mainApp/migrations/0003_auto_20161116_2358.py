# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gem',
            name='image',
            field=models.ImageField(blank=True, upload_to='gems'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20161213_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='prof_desc',
            field=models.CharField(default='', max_length=100),
        ),
    ]

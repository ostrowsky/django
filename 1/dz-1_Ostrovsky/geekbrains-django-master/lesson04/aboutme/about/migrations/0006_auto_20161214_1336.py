# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20161213_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]
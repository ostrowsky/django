# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hobby',
        ),
        migrations.DeleteModel(
            name='Study',
        ),
        migrations.RemoveField(
            model_name='work',
            name='organization',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
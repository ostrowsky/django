# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 10:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20170123_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='link',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_aboutdescription_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutdescription',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
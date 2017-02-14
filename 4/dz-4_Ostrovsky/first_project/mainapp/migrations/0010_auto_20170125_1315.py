# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-25 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20170124_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Организация')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('tax_id', models.PositiveIntegerField(default=111111, verbose_name='ИНН')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('flag', models.BooleanField(default=False, verbose_name='Флаг')),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='region',
        ),
        migrations.RemoveField(
            model_name='work',
            name='site',
        ),
        migrations.AlterField(
            model_name='work',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Organization', verbose_name='Организация'),
        ),
    ]
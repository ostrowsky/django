from django.db import models

class Organization(models.Model):
    name = models.CharField(verbose_name='Название',max_length=32, unique=True)
    region = models.CharField(verbose_name='Регион',max_length=32, blank=True)
    tax_id = models.PositiveIntegerField(verbose_name='Регистрационный номер')
    site = models.URLField(verbose_name='Сайт',blank=True)

class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация')
    position = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Период')

class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)

class Study(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    date_start = models.DateField(verbose_name='Дата начала обучения')
    date_end = models.DateField(verbose_name='Дата окончания обучения')

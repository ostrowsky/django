from django.db import models


# Create your models here.
class Work(models.Model):
    organization = models.ForeignKey(Organisation, verbose_name='Организация', null=True)
    position = models.CharField(verbose_name='Должность', max_length=128)
    duties = models.TextField(verbose_name='Обязаности')
    period = models.CharField(verbose_name='Период работы работы', max_length=32)

class Education(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=128)
    period = models.CharField(verbose_name='Период обучения', max_length=32)
    spec = models.CharField(verbose_name='Специальность', max_length=32, blank=True)
    link = models.CharField(verbose_name='Ссылка', max_length=64, blank=True)

class Person(models.Model):
    name = models.CharField(verbose_name='ФИО', max_length=32)
    birthdate = models.DateField(verbose_name='Дата рождения')
    text = models.TextField(verbose_name='Текст')

class Hobby(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=32)
    img = models.ImageField(verbose_name='Иконка', upload_to='img/')

class Organization(models.Model):
    name = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    tax_id = models.PositiveIntegerField(verbose_name='ИНН', default=111111)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    flag = models.BooleanField(verbose_name='Флаг', default=False)
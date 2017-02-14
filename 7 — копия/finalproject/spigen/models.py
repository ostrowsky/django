from django.db import models

class Item(models.Model):
    article = models.CharField(verbose_name='Артикул', max_length=32, unique=True)
    name = models.CharField(verbose_name='Артикул', max_length=128, unique=True)
    category = models.ForeignKey('Category', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='static/pics/')

class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    link = models.URLField(verbose_name='Ссылка', max_length=128, unique=True)
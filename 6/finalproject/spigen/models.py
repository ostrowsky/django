from django.db import models

class Item(models.Model)
    article = models.CharField(verbose_name='Артикул', max_length=32, required=True, unique=True)
    name = models.CharField(verbose_name='Артикул', max_length=128, required=True, unique=True)
    category = models.ForeignKey(verbose_name='Категория', 'Category', required=True)
    price = models.IntegerField(verbose_name='Цена', max_length=5, required=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='static/pics/')

class Category(models.Model):
    name = models.CharField(verbose_name='Артикул', max_length=128, required=True, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
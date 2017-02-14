from django.db import models

class Item(models.Model):
    article = models.CharField(verbose_name='Артикул', max_length=32, unique=True)
    name = models.CharField(verbose_name='Наименование', max_length=256, unique=True)
    category = models.ForeignKey('Category', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='media/pics/')
    preview = models.ImageField(verbose_name='Превью', upload_to='media/pics/previews', blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    link = models.CharField(verbose_name='Ссылка', max_length=128, unique=True)

    def __str__(self):
        return self.name
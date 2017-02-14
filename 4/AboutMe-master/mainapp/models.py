from django.db import models

class Organization(models.Model):
    name = models.CharField(verbose_name='Название',max_length=32, unique=True)
    region = models.CharField(verbose_name='Регион',max_length=32, blank=True)
    tax_id = models.PositiveIntegerField(verbose_name='Регистрационный номер')
    site = models.URLField(verbose_name='Сайт',blank=True, db_index=True)
    flag = models.BooleanField(verbose_name='Флаг', default=False)

    def in_msk(self):
        return self.region == 'Москва'

    def __str__(self):
        return self.name

class Work(models.Model):
    #много ко много
    organization = models.ForeignKey(Organization, verbose_name='Организация', null=True)
    position = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Период')

    def __str__(self):
        return self.position

class Hobby(models.Model):
    name = models.CharField(verbose_name='Название', max_length=32)

class Study(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    date_start = models.DateField(verbose_name='Дата начала обучения')
    date_end = models.DateField(verbose_name='Дата окончания обучения')


from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt
from django.utils.timezone import localtime
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='documents/')
    prof_desc = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} {}'.format(self.user.last_name, self.user.first_name)


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Work(models.Model):
    user = models.ForeignKey(UserProfile)
    company = models.ForeignKey(Company)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return '{}, {}'.format(self.company, self.position)


class Description(models.Model):
    work = models.ForeignKey(Work)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Education(models.Model):
    LEVEL_CHOICES = (
        ('Среднее образование', 'Среднее образование'),
        ('Неоконченное высшее образование', 'Неоконченное высшее образование'),
    )
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile)

    def __str__(self):
        return self.institution


class AboutDescription(models.Model):
    user = models.ForeignKey(UserProfile)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        datetime = dt.strftime(localtime(self.post_date), '%d.%m.%Y %H:%M:%S')
        return '{} {}'.format(self.user, datetime)

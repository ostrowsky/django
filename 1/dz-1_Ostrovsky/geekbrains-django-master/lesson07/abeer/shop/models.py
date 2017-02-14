from django.db import models
from django.conf import settings


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Product(models.Model):
    pass

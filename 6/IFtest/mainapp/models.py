from django.db import models

# Create your models here.
class Test(models.Model):
    image = models.ImageField(upload_to='test')

    def __str__(self):
        return self.image.url
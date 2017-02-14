from django.test import TestCase
from .models import Category


# Create your tests here.
class TestCategory(TestCase):
    def setUp(self):
        category1 = Category(name='Кварциты')
        category1.save()
        category2 = Category(name='Изумруды')
        category2.save()

    def testStr(self):
        category1 = Category.objects.get(name='Кварциты')
        category2 = Category.objects.get(name='Изумруды')
        self.assertEqual(str(category1), 'Кварциты  ')
        self.assertEqual(str(category2), 'Изумруды  ')

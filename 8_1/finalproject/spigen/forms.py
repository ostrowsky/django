from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Item


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя пользователя'}))
    email = forms.EmailField(required=True, label='Адрес e-mail', help_text='Адрес должен содержать символ @', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Адрес e-mail'}))
    first_name = forms.CharField(required=False, label='Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
    last_name = forms.CharField(required=False, label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')



'''
class UserChangeForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    email = forms.EmailField(required=True, label='Адрес e-mail', help_text='Адрес должен содержать символ @', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес e-mail'}))
    first_name = forms.CharField(required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')
'''

class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

class Item_form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('__all__')


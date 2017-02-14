from django import forms
from .models import UserProfile


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'birth_date']

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for value in self.fields.values():
            value.widget.attrs['class'] = 'form-control'

    def clean(self, *args, **kwargs):
        cleaned_data = super(RegistrationForm, self).clean(*args, **kwargs)
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

import email
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    pass

class SigninForm(UserCreationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
from django import forms
from django.forms import ModelForm
from .models import ExampleModel, Question, Choice

class ExampleModelForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    email = forms.EmailField()
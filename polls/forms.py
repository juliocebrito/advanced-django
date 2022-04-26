from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import ExampleModel, Question, Choice

class ExampleModelForm(forms.Form):
    name = forms.CharField(label='name', max_length=200)
    email = forms.EmailField()


class QuestionForm(ModelForm):
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}), required=False)

    class Meta:
        model = Question
        fields = '__all__'
        exclude = ('count_choices',)


class ChoiceForm(ModelForm):
    pass 
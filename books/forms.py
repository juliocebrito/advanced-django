from django import forms
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Author, Book

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']


class AuthorForm(forms.ModelForm):
    title = forms.ChoiceField(widget=forms.RadioSelect, choices=Author.TITLE_CHOICES)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('name must be longer!!')
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if name and name.isdigit():
            msg = 'Name can not be a number! - Author'
            self.add_error('name', msg)
        return cleaned_data



class BookForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '500'}))

    class Meta:
        model = Book
        fields = ['name', 'authors']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        print(user)
        super(BookForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name.isdigit():
            raise ValidationError('Name can not be a number! - Book')
        return cleaned_data

    def save(self):
        name = self.cleaned_data.get('name')
        if name:
            name = name + 's'
        self.instance.name = name
        self.instance.save()
        return self.instance
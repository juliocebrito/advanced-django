from django.contrib import admin

from advanced_django.utils import BaseModelAdmin
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)

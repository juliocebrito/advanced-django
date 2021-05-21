from django.db import models

from advanced_django.utils import BaseModel


class Author(BaseModel):
    TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    )
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    class Meta(BaseModel.Meta):
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return self.name


class Book(BaseModel):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    class Meta(BaseModel.Meta):
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.name

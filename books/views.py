from .models import Author, Book
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AuthorForm, BookForm


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/create_author')
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/create_book')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

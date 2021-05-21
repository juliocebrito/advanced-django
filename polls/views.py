from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExampleModel

from .forms import ExampleModelForm


def create_example_model(request):
    if request.method == 'POST':
        form = ExampleModelForm(request.POST)
        if form.is_valid():
            example = ExampleModel()
            example.name = form.cleaned_data['name']
            example.save()
            return HttpResponseRedirect('/polls/create_example_model')
    else:
        form = ExampleModelForm()
    return render(request, 'create_example_model.html', {'form': form})

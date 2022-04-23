from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExampleModel, Question
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ExampleModelForm, QuestionForm


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



class ListQuestionView(LoginRequiredMixin, ListView):
    login_url = 'users:home'
    model = Question
    template_name = 'polls/list_question.html'


class CreateQuestionView(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = QuestionForm
    template_name = 'polls/create_question.html'


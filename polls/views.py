from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ExampleModel, Question
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['qty'] = Question.objects.all().count()
        context['yes'] = 10
        context['no'] = 12
        return context


class CreateQuestionView(LoginRequiredMixin, CreateView):
    login_url = 'users:home'
    form_class = QuestionForm
    template_name = 'polls/create_question.html'
    success_url = reverse_lazy('polls:list_question')

class DetailQuestionView(LoginRequiredMixin, DetailView):
    login_url= 'users:home'
    model = Question
    template_name = 'polls/detail_question.html'



class UpdateQuestionView(LoginRequiredMixin, UpdateView):
    login_url = 'users:home'
    model = Question
    form_class = QuestionForm
    template_name = 'polls/update_question.html'
    success_url = reverse_lazy('polls:list_question')

class DeleteQuestionView(LoginRequiredMixin, DeleteView):
    login_url = 'users:home'
    model = Question
    template_name = 'polls/delete_question.html'
    success_url = reverse_lazy('polls:list_question')
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, RedirectView, FormView
from .forms import LoginForm, SigninForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'users/home.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('users:home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class SigninView(CreateView):
    form_class = SigninForm
    model = User
    template_name = 'users/signin.html'
    success_url = reverse_lazy('users:home')
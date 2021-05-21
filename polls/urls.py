from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('create_example_model', views.create_example_model, name='create_example_model'),
    # path('', views.polls, name='polls'),
]
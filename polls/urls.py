from django.urls import path

from . import views
from .views import ListQuestionView, CreateQuestionView

app_name = 'polls'

urlpatterns = [
    path('create_example_model', views.create_example_model, name='create_example_model'),
    # path('', views.polls, name='polls'),
    path('list_question/', ListQuestionView.as_view(), name='list_question'),
    path('create_question/', CreateQuestionView.as_view(), name='create_question'),
]
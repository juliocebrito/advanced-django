from django.urls import path

from . import views
from .views import (ListQuestionView, CreateQuestionView, 
DetailQuestionView, UpdateQuestionView, DeleteQuestionView)

app_name = 'polls'

urlpatterns = [
    path('create_example_model', views.create_example_model, name='create_example_model'),
    # path('', views.polls, name='polls'),
    path('list_question/', ListQuestionView.as_view(), name='list_question'),
    path('create_question/', CreateQuestionView.as_view(), name='create_question'),
    path('detail_question/<int:pk>/', DetailQuestionView.as_view(), name='detail_question'),
    path('update_question/<int:pk>/', UpdateQuestionView.as_view(), name='update_question'),
    path('delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
]
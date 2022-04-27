from django.urls import path

from . import views
from .views import (ListQuestionView, CreateQuestionView, 
DetailQuestionView, UpdateQuestionView, DeleteQuestionView)

app_name = 'polls'

urlpatterns = [
    # CRUD VIEWS (CREATE, READ[LIST, DETAIL], UPDATE, DELETE)

    path('create_example_model/', views.create_example_model, name='create_example_model'),
    path('list_example_model/', views.list_example_model, name='list_example_model'),
    path('detail_example_model/<int:pk>/', views.detail_example_model, name='detail_example_model'),
    path('update_example_model/<int:pk>/', views.update_example_model, name='update_example_model'),
    path('delete_example_model/<int:pk>/', views.delete_example_model, name='delete_example_model'),

    # CRUD CLASS-BASED VIEWS (CREATE, READ[LIST, DETAIL], UPDATE, DELETE)
    
    path('create_question/', CreateQuestionView.as_view(), name='create_question'),
    path('list_question/', ListQuestionView.as_view(), name='list_question'),
    path('detail_question/<int:pk>/', DetailQuestionView.as_view(), name='detail_question'),
    path('update_question/<int:pk>/', UpdateQuestionView.as_view(), name='update_question'),
    path('delete_question/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
]
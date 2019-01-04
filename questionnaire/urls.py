from django.urls import path
from . import views

urlpatterns = [
    path('questions', views.init_question_page, name='Initial Page'),
]
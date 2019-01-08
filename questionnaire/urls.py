# Django
from django.urls import path

# Local Django
from questionnaire.views import QuestionView,AnswerView

urlpatterns = [
    path('questions', QuestionView.as_view(), name='Initial Page'),
    path('answers', AnswerView.as_view(), name='Initial Page'),
]
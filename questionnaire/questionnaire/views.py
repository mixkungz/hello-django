import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import QuizForm
from .models import Question, Choices, Answer
# Create your views here.


class QuestionView(View):

    def get(self, request):
        form = QuizForm()
        questions = Question.objects.all()

        for question in questions:
            choices = list(question.choices.all())
            question.choice_list = choices

        return render(request, 'question_list.html', {'question_lists': questions, 'form': form})

    def post(self, request):
        dict_request = dict(request.POST)
        del dict_request['csrfmiddlewaretoken']

        for key in dict_request:
            id = key[12:]
            for answer in dict_request[key]:
                try:
                    question = Question.objects.get(id=id)
                    answer = Choices.objects.get(id=answer)
                    Answer.objects.create(
                        question_id=question, choice_id=answer)
                except:
                    return render(request, 'failed.html')

        return render(request, 'success.html')


class AnswerView(View):
    def get(self, request):
        answers = Answer.objects.all()
        return render(request, 'answers.html', {'answers': answers})

    def post(self, request):
        Answer.objects.all().delete()
        return redirect('/answers')

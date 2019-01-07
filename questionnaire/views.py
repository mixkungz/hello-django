import json
from django.shortcuts import render,redirect
from .models import Question, Choices, QuestionChoice, Answer
# Create your views here.

def init_question_page(request):
    if(request.method == 'POST'):
        dict_request = dict(request.POST)
        del dict_request['csrfmiddlewaretoken']
        for key in dict_request:
            id = key[12:]
            for answer in dict_request[key]:
                try:
                    question = Question.objects.get(id=id)
                    answer = Choices.objects.get(id=answer)
                    Answer.objects.create(question_id=question,choice_id=answer)
                except:
                    return render(request,'failed.html')
        return render(request,'success.html')
    
    questions = Question.objects.all()
    return_data = []

    for question in questions:
        choices = QuestionChoice.objects.filter(question_id=question.id).values('choice_id','choice_id__choice')
        choices = list(choices)

        prepare_data = {
            "question_id":question.id,
            "question_name":question.question,
            "choices":choices
        }
        return_data.append(prepare_data)

    return render(request, 'question_list.html',{'question_lists':return_data})

def init_answer_page(request):
    if(request.method == 'POST'):
        Answer.objects.all().delete()
        return redirect('/answers')

    answers = Answer.objects.all()
    return render(request, 'answers.html',{'answers':answers})

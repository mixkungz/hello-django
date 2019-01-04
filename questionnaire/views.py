import json
from django.shortcuts import render
from .models import Question, Choices, QuestionChoice, Answer
# Create your views here.

def init_question_page(request):

    if(request.method == 'POST'):
        dict_request = dict(request.POST)
        del dict_request['csrfmiddlewaretoken']

        for key in dict_request:
            id = key[12:]
            print(key.split('question_id_')[1])


    

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
    return render(request, 'answers.html')

# [
#     {
#         question_id:1,
#         question_name:'1+1 = ?',
#         choices:[
#             id:1,
#             choice:'up to me'
#         ]
#     }
# ]

# [
#     [{คำถาม},{ช้อย}],
#     [{คำถาม},{ช้อย}],
#     [{คำถาม},{ช้อย}],
#     [{คำถาม},{ช้อย}],
# ]

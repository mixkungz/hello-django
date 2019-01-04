from django.shortcuts import render

# Create your views here.

def init_question_page(request):
    return render(request,'question_list.html')
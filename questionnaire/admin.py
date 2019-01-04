from django.contrib import admin
from .models import Question, Choices, QuestionChoice, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(QuestionChoice)
admin.site.register(Answer)
# Django
from django.contrib import admin

# Local
from .models import Question, Choices, QuestionChoice, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at', 'updated_at']

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['choice', 'created_at', 'updated_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(QuestionChoice)
admin.site.register(Answer)


# Django
from django.contrib import admin

# Local
from .models import Question, Choices, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at', 'updated_at']

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice', 'created_at', 'updated_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choices, ChoicesAdmin)
admin.site.register(Answer)


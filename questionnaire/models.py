from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question


class Choices(models.Model):
    id = models.AutoField(primary_key=True)
    choice = models.TextField()

    def __str__(self):
        return self.choice


class QuestionChoice(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choices, on_delete=models.CASCADE, default=0)

    class Meta:
        unique_together = (('question_id', 'choice_id'))


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choices, on_delete=models.CASCADE, default=0)

    class Meta:
        unique_together = (('question_id', 'choice_id'))
    


from django.test import TestCase
from questionnaire.models import Question, Choices, Answer


class AnswerTest(TestCase):
    def setUp(self):
        question = Question.objects.create(question='1+1 = ?')
        choice = Choices.objects.create(choice='2')

        # Add Choice into Question
        question.choices.add(choice)

        Answer.objects.create(question_id=question, choice_id=choice)

    def test_last_question_was_answered_with_the_last_choice_should_not_return_none(self):
        last_question = Question.objects.last()
        last_choice = Choices.objects.last()
        last_answer = Answer.objects.get(
            question_id=last_question, choice_id=last_choice)

        self.assertNotEqual(last_answer, None)

    # def test_answer_that_has_question_id_1_and_has_choice_id_1_must_not_none(self):
    #     answer = Answer.objects.get(question_id=1, choice_id=1)
    #     self.assertNotEqual(answer, None)

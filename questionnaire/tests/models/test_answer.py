from django.test import TestCase
from questionnaire.models import Question, Choices, Answer

class AnswerTest(TestCase):
    def setUp(self):
        question1 = Question.objects.create(question='1+1 = ?')
        choice1 = Choices.objects.create(choice='2')
        choice2 = Choices.objects.create(choice='22')
        choice3 = Choices.objects.create(choice='2222')
        choice4 = Choices.objects.create(choice='222')

        question2 = Question.objects.create(question='22 = ?')
        choice5 = Choices.objects.create(choice='-22')
        choice6 = Choices.objects.create(choice='-222')
        choice7 = Choices.objects.create(choice='-2222')
        #Add Choice into Question
        question1.choices.add(choice1, choice2, choice3, choice4)
        question2.choices.add(choice2, choice3, choice4, choice5)
        
        Answer.objects.create(question_id=question1, choice_id=choice1)
        Answer.objects.create(question_id=question2, choice_id=choice2)

    def test_answer_that_has_question_id_1_and_has_choice_id_1_must_not_none(self):
        answer = Answer.objects.get(question_id=1,choice_id=1)
        self.assertNotEqual(answer, None)

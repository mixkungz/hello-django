from django.urls import reverse
from django.test import TestCase, Client
from questionnaire.models import Question, Choices, Answer


class QuestionViewTest(TestCase):
    # def setUp(self):
    #     self.client = Client()

    def test_question_view_get_method(self):
        question1 = Question.objects.create(question='Germany = ?')
        choice1 = Choices.objects.create(choice='2')
        choice2 = Choices.objects.create(choice='22')
        choice3 = Choices.objects.create(choice='2222')
        choice4 = Choices.objects.create(choice='222')
        question1.choices.add(choice1, choice2, choice3, choice4)

        response = self.client.get(reverse('question_view'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question_list.html')
        self.assertContains(response, 'Germany = ?')

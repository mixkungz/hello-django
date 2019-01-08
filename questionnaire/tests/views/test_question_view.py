from django.urls import reverse
from django.test import TestCase, Client

class QuestionViewTest(TestCase):
    # def setUp(self):
    #     self.client = Client()

    def test_question_view_get_method(self):
        response = self.client.get(reverse('question_view'))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'question_list.html')
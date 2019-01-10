from django.test import TestCase
from questionnaire.models import Question

class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(question='1+1 = ?')
        Question.objects.create(question='a b then ?')

    def test_id_1_should_has_question_name_1plus1equal(self):
        question_1 = Question.objects.get(id=1)
        self.assertEqual(question_1.question, '1+1 = ?')

    def test_question_name_abthen_has_id_2(self):
        abthen = Question.objects.get(id=2)
        self.assertEqual(abthen.id, 2)



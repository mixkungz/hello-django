from django.test import TestCase
from questionnaire.models import Choices

class ChoicesTest(TestCase):
    def setUp(self):
        Choices.objects.create(choice='uniqlo')
        Choices.objects.create(choice='h&m')

    def test_choice_uniqlo_should_has_id_1(self):
        uniqlo = Choices.objects.get(choice='uniqlo')
        self.assertEqual(uniqlo.id, 1)

    def test_choice_handm_should_has_id_2(self):
        ham = Choices.objects.get(choice='h&m')
        self.assertEqual(ham.id, 2)



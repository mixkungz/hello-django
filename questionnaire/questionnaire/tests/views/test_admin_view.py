# Django
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import TestCase, Client

# Local
from questionnaire.admin import QuestionAdmin, ChoicesAdmin
from questionnaire.models import Question, Choices, Answer


class MockRequest:
    pass


class MockSuperUser:
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()


class TestContributorAdmin(TestCase):
    def setUp(self):
         self.site = AdminSite()


    def test_should_show_column_defined(self):
        question_expected = ['question', 'choices']
        question_model_admin = ModelAdmin(Question, self.site)

        self.assertEqual(list(question_model_admin.get_fields(request)), question_expected)

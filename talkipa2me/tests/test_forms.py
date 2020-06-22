from django.test import TestCase
from pytest import mark

from talkipa2me.forms import IndexForm, IssuesForm


class TestIndexForm(TestCase):
    @mark.django_db()
    def test_form_valid(self):
        form = IndexForm({'text_area': 'hello,;. world!'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = IndexForm({'text_area': ''})
        self.assertFalse(form.is_valid())


class TestIssuesForm(TestCase):
    @mark.django_db()
    def test_form_valid(self):
        form = IssuesForm({'name': 'A', 'email': 'example@example.com', 'message': 'A'})
        self.assertTrue(form.is_valid())

    def test_name_invalid(self):
        form = IndexForm({'name': '', 'email': 'example@example.com', 'message': 'A'})
        self.assertFalse(form.is_valid())

    def test_email_invalid(self):
        form = IssuesForm({'name': 'A', 'email': 'example@example.', 'message': 'A'})
        self.assertFalse(form.is_valid())

    def test_message_invalid(self):
        form = IssuesForm({'name': 'A', 'email': 'example@example.', 'message': ''})
        self.assertFalse(form.is_valid())

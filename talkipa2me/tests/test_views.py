from django.core import mail
from django.test import TestCase
from django.urls import reverse_lazy
from pytest import mark


class TestIndex(TestCase):
    @mark.django_db()
    def test_translation(self):
        response = self.client.post('', {'text_area': 'hello,;. world!'})
        self.assertEqual(response.context["text"], "Həl'oʊ,;. wɜrld!")


class TestIssues(TestCase):
    @mark.django_db()
    def test_email(self):
        name = 'Test Name'
        email = 'test@email.com'
        subject = 'Test Subject'
        message = 'Test message'
        data = {'name': name, 'email': email, 'subject': subject, 'message': message}
        response = self.client.post(reverse_lazy('issues'), data)
        return response

    def test_renders_answer(self):
        response = self.test_email()
        self.assertEqual(response.context["answer"], 'Test')

    def test_email_in_outbox(self):
        response = self.test_email()
        self.assertEqual(len(mail.outbox), 1)

    def test_correct_subject(self):
        response = self.test_email()
        self.assertEqual(mail.outbox[0].subject, 'Test Name: test@email.com')
from django.core import mail
from django.test import TestCase
from django.urls import reverse_lazy
from pytest import mark


class TestIndex(TestCase):
    @mark.django_db()
    def test_translation(self):
        response = self.client.post('', {'text_area': 'hello,;. world!'})
        self.assertEqual(response.context["text"], "Həl'oʊ,;. wɜrld!")
# Headless browser // Selenenium -> look up for remote testing Sauce labs
# Parameterized tests // DDT data driven tests
# Test functions.py

class TestIssues(TestCase):
    @mark.django_db()
    def setUp(self):
        name = 'Test Name'
        email = 'test@email.com'
        subject = 'Test Subject'
        message = 'Test message'
        data = {'name': name, 'email': email, 'subject': subject, 'message': message}
        self.response = self.client.post(reverse_lazy('issues'), data)
        #mail gun, Amazon SES, sendgrid

    def test_renders_answer(self):
        self.assertEqual(self.response.context["answer"], 'Test')

    def test_email_in_outbox(self):
        self.assertEqual(len(mail.outbox), 1)

    def test_correct_subject(self):
        self.assertEqual(mail.outbox[0].subject, 'Test Name: test@email.com')


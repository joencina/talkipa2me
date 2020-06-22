from django.test import TestCase
from pytest import mark


class TestIndexForm(TestCase):
    @mark.django_db()
    def test_translation(self):
        response = self.client.post('', {'text_area': 'hello,;. world!'})
        self.assertEqual(response.context["text"], "Həl'oʊ,;. wɜrld!")

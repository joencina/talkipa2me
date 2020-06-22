from django.test import TestCase
from pytest import mark

from talkipa2me.forms import IndexForm


class TestIndexForm(TestCase):
    @mark.django_db()
    def test_form_valid(self):
        form = IndexForm({'text_area': 'hello,;. world!'})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = IndexForm({'text_area': ''})
        self.assertFalse(form.is_valid())


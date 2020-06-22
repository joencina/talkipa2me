import unittest

from django.test import SimpleTestCase
from django.urls import reverse


class IndexTest(SimpleTestCase):
    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Get text in IPA')

    def test_bulma_css(self):
        response = self.client.get('/static/bulma/css/style.min.css')
        self.assertEqual(response.status_code, 200)

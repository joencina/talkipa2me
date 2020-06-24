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
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Get text in IPA')


class IssuesTest(SimpleTestCase):
    def test_issues_status_code(self):
        response = self.client.get('/issues')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('issues'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('issues'))
        self.assertTemplateUsed(response, 'issues.html')

    def test_issues_contains_correct_html(self):
        response = self.client.get('/issues')
        self.assertContains(response, 'Submit an issue')


class WhatIsTest(SimpleTestCase):
    def test_what_is_status_code(self):
        response = self.client.get('/what_is')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('what_is'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('what_is'))
        self.assertTemplateUsed(response, 'what_is.html')

    def test_issues_contains_correct_html(self):
        response = self.client.get('/what_is')
        self.assertContains(response, 'What is IPA?')

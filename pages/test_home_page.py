from django.test import SimpleTestCase
from django.urls import reverse
from django.http import HttpResponse

class HomePageTestCase(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        resp = self.client.get('/')
        self.assertEqual(HttpResponse.status_code, resp.status_code)

    def test_url_exists_at_correct_location_reverse(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(HttpResponse.status_code, resp.status_code)

    def test_url_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp, 'home.html')

    def test_correct_template_content(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, '<h1>Homepage</h1>')

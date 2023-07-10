from django.test import SimpleTestCase
from django.http import HttpResponse
from django.urls import reverse

# Create your tests here.
class AboutPageTestCase(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        resp = self.client.get('/about/')
        self.assertEqual(HttpResponse.status_code, resp.status_code)

    def test_url_exists_at_correct_location_reverse(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(HttpResponse.status_code, resp.status_code)

    def test_url_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertTemplateUsed(resp, 'about.html')

    def test_correct_template_content(self):
        resp = self.client.get(reverse('about'))
        self.assertContains(resp, '<h1>About page</h1>')

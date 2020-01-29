from django.test import TestCase
from django.shortcuts import resolve_url as r

class CoreTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200."""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must user template index.html."""
        self.assertTemplateUsed(self.response, 'index.html')
from django.test import TestCase

class ProductListTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/produtos/')

    def test_get(self):
        """Must return status code 200"""
        self.assertAlmostEqual(200, self.response.status_code)

    def test_template(self):
        """Must use template product_list.html"""
        self.assertTemplateUsed(self.response, 'product_list.html')

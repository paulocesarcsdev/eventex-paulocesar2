from django.test import TestCase

# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        #response = self.client.get('/')
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        #response = self.client.get('/')
        self.assertTemplateUsed(self.resp, 'index.html')


from django.test import TestCase

# Add tests here.
class Test(SimpleTestCase):
  def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('spiderman')
        self.assertEqual(response.status_code, 200)

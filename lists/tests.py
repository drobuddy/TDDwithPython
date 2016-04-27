from django.core.urlresolvers import resolve
from django.test import TestCase
from django.request import HttpRequest
from lists.views import home_page

# Create your tests here.

class HomePageTest (TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)     # Resolve was able to map a function to the home_page view
        
    def test_home_page_returns_correct_HTML_view(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startsWith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endsWith(b'</html>'))



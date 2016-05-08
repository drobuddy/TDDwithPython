from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Use Tools.pp to nicely format data
# that we need returned to the console 
# for testing and diagnostics

from TestingHelpers import Tools
# Example usage:
# Tools.pp(response.content)


# Create your tests here.

class HomePageTest (TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)     # The "found" response contains a function called home_page
        
    def test_home_page_returns_correct_HTML_view(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
        
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


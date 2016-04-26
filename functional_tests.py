#!/usr/bin/python3

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):


        # Edith has heard about a cool new online web app. She goes
        # to check out it's webpage.
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buying peacock feathers" into the textbox (Edith's hobby
        # is making fly-fishing lures).

        # When she hits, "Enter" the page updates, and now the page lists:
        # "1. Buy peacock feathers" as an item on the to-do list

        # There is still a textbox inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical).

        # The page updates, and now both items are shown on her list

        # Edith wonders if the site will remember her list. Then she sees the
        # site has generated a unique URL for her -- there is some explanatory
        # text to that effect.

        # She visits the URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.
        self.browser.quit()

if __name__ == '__main__': unittest.main(warnings='ignore')

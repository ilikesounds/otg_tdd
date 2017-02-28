from selenium import webdriver
import unittest


"""
Suck it docstrings!!!
"""

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')
# assert 'to-do' in browser.title, "Browser title was " + browser.title
# browser.quit()


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """
        This setup function specifies that the browser used for functional
        testing is the firefox browser
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        This tear down function has the browser quit after the functional
        test has run
        """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        This function is the actual functional testing
        """
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

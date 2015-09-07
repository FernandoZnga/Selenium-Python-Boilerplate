import unittest
from selenium import webdriver


class TestHeadless(unittest.TestCase):
    """
    Basic test case that uses PhantomJS as driver
    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_title(self):
        self.driver.get("http://www.tomwaits.com")
        self.assertEquals("Tom Waits", self.driver.title)

    def tearDown(self):
        self.driver.quit()

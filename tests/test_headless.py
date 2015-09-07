import unittest
from selenium import webdriver


class TestHeadless(unittest.TestCase):
    """
    Basic test case that uses PhantomJS as driver
    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1024, 768)

    def test_title(self):
        self.driver.get("http://www.tomwaits.com")
        self.assertEquals("Tom Waits", self.driver.title)

    def test_url(self):
        self.driver.get("http://www.tomwaits.com")
        self.assertEquals(self.driver.current_url, "http://www.tomwaits.com/")

    def tearDown(self):
        self.driver.quit()

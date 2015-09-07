import unittest
from pyvirtualdisplay import Display
from selenium import webdriver


class TestFirefox(unittest.TestCase):
    """
    Basic test case that uses firefox as a driver.
    """

    def setUp(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()

        self.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get("http://www.tomwaits.com")
        self.assertEquals("Tom Waits", self.driver.title)

    def test_url(self):
        self.driver.get("http://tomwaits.com")
        self.assertEquals(self.driver.current_url, "http://www.tomwaits.com/")

    def tearDown(self):
        self.driver.quit()
        self.display.stop()

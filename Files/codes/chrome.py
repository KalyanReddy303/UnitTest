import unittest
from selenium import webdriver


class TestOpening(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        driver = self.driver
        driver.get("https://docs.python.org/3/library/unittest.html")
        driver.maximize_window()

    def test_opening_browser(self):
        self.assertEqual(10, 10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

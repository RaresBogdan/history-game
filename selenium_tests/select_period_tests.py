from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

# NOTE: In order to access the select period page, the user must be logged in.


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        service = Service(r'')    # Add the path to your local installation of Google Chrome Driver
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class TestSelectPeriodPage(BaseTestCase):

    def test_select_prehistory(self):
        self.driver.get('http://127.0.0.1:5000/select_period')

        # Click on the prehistory selector button
        prehistory_button = self.driver.find_element(By.ID, "buttonPre")
        prehistory_button.click()
        time.sleep(3)

        # Assert that you are redirected to the correct page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/guessing_game/prehistory")

    def test_select_ancient_history(self):
        self.driver.get('http://127.0.0.1:5000/select_period')

        # Click on the ancient history selector button
        ancient_history_button = self.driver.find_element(By.ID, "buttonAncient")
        ancient_history_button.click()
        time.sleep(3)

        # Assert that you are redirected to the correct page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/guessing_game/ancient%20history")

    def test_select_post_classical_history(self):
        self.driver.get('http://127.0.0.1:5000/select_period')

        # Click on the post classical history selector button
        post_classical_history_button = self.driver.find_element(By.ID, "buttonPCH")
        post_classical_history_button.click()
        time.sleep(3)

        # Assert that you are redirected to the correct page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/guessing_game/post-classical%20history")

    def test_select_modern_history(self):
        self.driver.get('http://127.0.0.1:5000/select_period')

        # Click on the modern history selector button
        modern_history_button = self.driver.find_element(By.ID, "buttonModern")
        modern_history_button.click()
        time.sleep(3)

        # Assert that you are redirected to the correct page
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:5000/guessing_game/modern%20history")


if __name__ == '__main__':
    unittest.main()

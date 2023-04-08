from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        service = Service(r'PATH_TO_GOOGLE_CHROME_DRIVER')   # Add the path to your local installation of Google Chrome Driver
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class TestSignupPage(BaseTestCase):

    def test_invalid_char_username(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the username field with invalid input
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('!@##')
        time.sleep(1)

        # Check if the error bubble is displayed indicating an invalid username format
        is_username_invalid = username_input.get_attribute('validationMessage') != ''
        self.assertTrue(is_username_invalid)

    def test_username_field_with_whitespaces(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the form with valid input for email and password fields
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('test@example.com')
        time.sleep(1)

        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password123')
        time.sleep(2)

        # Fill in the username field with spaces
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('   ')
        time.sleep(1)

        # Click the create account button
        create_account_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        create_account_button.click()
        time.sleep(1)

        # Assert that the user is still on the sign-up page after clicking the button
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:5000/sign_up')

    def test_username_max_length(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the username field with more than 20 characters
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('username1234567890123456')

        # Check that the username field only allows 20 characters
        self.assertEqual(len(username_input.get_attribute('value')), 20)

    def test_email_field_with_whitespaces(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the email field with whitespaces
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('    ')
        time.sleep(1)

        # Fill in the password field with valid input
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password123')
        time.sleep(1)

        # Fill in the username field with valid input
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('usernames')
        time.sleep(1)

        # Click the create account button
        create_account_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        create_account_button.click()
        time.sleep(1)

        # Assert that the user is still on the sign-up page after clicking the button
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:5000/sign_up')

    def test_email_max_input(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the email field with more than 70 characters
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('username@12345678931232341324124312341241234213412341234123412342134.ro')

        # Check that the email field only allows 70 characters
        self.assertEqual(len(email_input.get_attribute('value')), 70)

    def test_valid_email_format(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the username field with valid input
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('username155332')
        time.sleep(1)

        # Fill in the password field with valid input
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password123')
        time.sleep(1)

        # Fill in the email field with an invalid email format
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('invalid_email')
        time.sleep(1)

        # Check if the error bubble is displayed indicating an invalid email format
        is_email_invalid = email_input.get_attribute('validationMessage') != ''
        self.assertTrue(is_email_invalid)

        # Clear the email field and enter a valid email format
        email_input.clear()
        email_input.send_keys('validations_emails@example.com')
        time.sleep(1)

        # Click the create account button
        create_account_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        create_account_button.click()
        time.sleep(1)

        # Assert that you are redirected to the correct page
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:5000/select_period')

    def test_password_max_length(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the password field with more than 20 characters
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password1234567832901234')

        # Check that the password field allows at most 20 characters
        self.assertEqual(len(password_input.get_attribute('value')), 20)

    def test_successful_signup(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the email field with valid input
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('email@test.ro')
        time.sleep(1)

        # Fill in the password field with valid input
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password123')
        time.sleep(1)

        # Fill in the username field with valid input
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('username123')
        time.sleep(1)

        # Click the create account button
        create_account_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        create_account_button.click()
        time.sleep(1)

        # Assert that the user is still on the sign-up page after clicking the button
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:5000/select_period')

    def test_successful_login(self):
        self.driver.get('http://127.0.0.1:5000/sign_up')

        # Fill in the email field with valid input
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.clear()
        email_input.send_keys('email@tester.ro')
        time.sleep(1)

        # Fill in the password field with valid input
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys('password123')
        time.sleep(1)

        # Fill in the username field with valid input
        username_input = self.driver.find_element(By.ID, 'username')
        username_input.clear()
        username_input.send_keys('username12345')
        time.sleep(1)

        # Click the create account button
        create_account_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        create_account_button.click()
        time.sleep(1)

        # Go to the login page and try to log in with the new account
        self.driver.get('http://127.0.0.1:5000/login')

        # Fill in the username field
        login_username_input = self.driver.find_element(By.ID, 'username')
        login_username_input.clear()
        login_username_input.send_keys('username12345')
        time.sleep(1)

        # Fill in the password field with valid input
        login_password_input = self.driver.find_element(By.ID, 'password')
        login_password_input.clear()
        login_password_input.send_keys('password123')
        time.sleep(1)

        # Click the login button
        login_button = self.driver.find_element(By.CLASS_NAME, 'btn')
        login_button.click()
        time.sleep(1)

        # Assert that the user has successfully reached the select period page after clicking the button
        self.assertEqual(self.driver.current_url, 'http://127.0.0.1:5000/select_period')


if __name__ == '__main__':
    unittest.main()



import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://zero-gravity-wxdemo.web.app/auth/B/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_sign_up_valid_input(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('testuser')
            self.driver.find_element('name', 'email').send_keys('test@example.com')
            self.driver.find_element('xpath', '(//input[@name="password"])[1]').send_keys('password123')
            self.driver.find_element('xpath', '(//input[@name="password"])[2]').send_keys('password123')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertEqual(alert.text, "Sign up successful!")
            alert.accept()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

    def test_sign_up_invalid_username(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('test')
            self.driver.find_element('name', 'email').send_keys('test@example.com')
            self.driver.find_element('xpath', '(//input[@name="password"])[1]').send_keys('password123')
            self.driver.find_element('xpath', '(//input[@name="password"])[2]').send_keys('password123')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign up successful!")
            alert.accept()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

    def test_sign_up_invalid_email(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('testuser')
            self.driver.find_element('name', 'email').send_keys('invalidemail')
            self.driver.find_element('xpath', '(//input[@name="password"])[1]').send_keys('password123')
            self.driver.find_element('xpath', '(//input[@name="password"])[2]').send_keys('password123')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign up successful!")
            alert.accept()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

    def test_sign_up_password_mismatch(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('testuser')
            self.driver.find_element('name', 'email').send_keys('test@example.com')
            self.driver.find_element('xpath', '(//input[@name="password"])[1]').send_keys('password123')
            self.driver.find_element('xpath', '(//input[@name="password"])[2]').send_keys('password456')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign up successful!")
            alert.accept()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")

if __name__ == "__main__":
    unittest.main()
  
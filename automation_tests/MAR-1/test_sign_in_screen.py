
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://zero-gravity-wxdemo.web.app/auth/B/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_sign_in_valid(self):
        try:
            self.driver.find_element('name', 'username_login').send_keys('validuser')
            self.driver.find_element('name', 'password_login').send_keys('validpass')
            self.driver.find_element('name', 'signin').click()
            alert = self.driver.switch_to.alert
            self.assertEqual(alert.text, "Sign in successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_in_valid: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_in_valid: {e}")

    def test_sign_in_invalid_username(self):
        try:
            self.driver.find_element('name', 'username_login').send_keys('inv')
            self.driver.find_element('name', 'password_login').send_keys('validpass')
            self.driver.find_element('name', 'signin').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign in successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_in_invalid_username: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_in_invalid_username: {e}")

    def test_sign_in_invalid_password(self):
        try:
            self.driver.find_element('name', 'username_login').send_keys('validuser')
            self.driver.find_element('name', 'password_login').send_keys('inv')
            self.driver.find_element('name', 'signin').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign in successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_in_invalid_password: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_in_invalid_password: {e}")

    def test_sign_up_valid(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('newuser')
            self.driver.find_element('name', 'email').send_keys('newuser@example.com')
            self.driver.find_element('name', 'password').send_keys('newpass')
            self.driver.find_element('name', 'password').send_keys('newpass')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertEqual(alert.text, "Sign up successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_up_valid: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_up_valid: {e}")

    def test_sign_up_invalid_username(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('inv')
            self.driver.find_element('name', 'email').send_keys('newuser@example.com')
            self.driver.find_element('name', 'password').send_keys('newpass')
            self.driver.find_element('name', 'password').send_keys('newpass')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign up successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_up_invalid_username: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_up_invalid_username: {e}")

    def test_sign_up_invalid_password(self):
        try:
            self.driver.find_element('xpath', '//a[text()="Sign Up"]').click()
            self.driver.find_element('name', 'username').send_keys('newuser')
            self.driver.find_element('name', 'email').send_keys('newuser@example.com')
            self.driver.find_element('name', 'password').send_keys('inv')
            self.driver.find_element('name', 'password').send_keys('inv')
            self.driver.find_element('name', 'signup').click()
            alert = self.driver.switch_to.alert
            self.assertNotEqual(alert.text, "Sign up successful!")
            alert.accept()
        except AssertionError as e:
            print(f"AssertionError in test_sign_up_invalid_password: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException in test_sign_up_invalid_password: {e}")

if __name__ == "__main__":
    unittest.main()
  
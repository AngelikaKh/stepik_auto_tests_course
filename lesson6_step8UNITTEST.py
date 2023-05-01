import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        first_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        last_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        email_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")

        elements = [first_name_input, last_name_input, email_input]

        for element in elements:
            element.send_keys("Bla-bla-bla")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        first_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        last_name_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        email_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")

        elements = [first_name_input, last_name_input, email_input]

        for element in elements:
            element.send_keys("Bla-bla-bla")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()

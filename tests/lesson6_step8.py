from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    last_name_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    email_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")

    elements = [first_name_input, last_name_input, email_input]

    for element in elements:
        element.send_keys("Bla-bla-bla")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

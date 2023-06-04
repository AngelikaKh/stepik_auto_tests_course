from selenium.webdriver.common.by import By
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_displayed(browser):
    browser = webdriver.Chrome()
    browser.get(link)
    # time.sleep(5)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button, "Button is not presented"

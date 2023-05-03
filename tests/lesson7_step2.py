from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Вычисляем значение функции и вводим ответ в текстовое поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None

    time.sleep(10)

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_disabled = submit.get_attribute("disabled")
    print("state of submit button is: ", submit_disabled)
    assert submit_disabled is None

finally:
    time.sleep(3)
    browser.quit()



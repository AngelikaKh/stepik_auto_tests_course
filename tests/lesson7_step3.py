from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

try:
    # Считываем значение x
    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    treasure_valuex = treasure.get_attribute("valuex")
    x = treasure_valuex

    # Вычисляем значение функции и вводим ответ в текстовое поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()

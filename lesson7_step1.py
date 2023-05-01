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

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    time.sleep(3)
    browser.quit()



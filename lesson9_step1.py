from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x_el):
    return str(math.log(abs(12 * math.sin(int(x_el)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:
    btn = browser.find_element(By.XPATH, "//button[@type='submit']")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = int(x_element.text)

    # print(x_element.text)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))

    # print(answer.text)

    # print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(30)
    browser.quit()


# alert = browser.switch_to.alert
# alert_text = alert.text

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()


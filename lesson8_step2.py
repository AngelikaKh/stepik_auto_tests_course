from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    # browser.get("http://suninjuly.github.io/selects2.html")

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sumOfNum = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sumOfNum))

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

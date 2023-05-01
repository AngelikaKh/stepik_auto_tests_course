from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    # browser.get("http://suninjuly.github.io/huge_form.html")
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Bla-bla-bla")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
#
# //input[contains(@placeholder,'name') and contains(@placeholder,'email')]
# //input[@required]
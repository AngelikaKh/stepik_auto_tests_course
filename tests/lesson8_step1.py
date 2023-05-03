from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
# browser.get("http://suninjuly.github.io/selects2.html")

browser.find_element(By.TAG_NAME, "select").click()
# browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# or browser.find_element(By.CSS_SELECTOR, "[value='1']").click()

# Это не самый удобный способ, так как нам приходится делать лишний клик для открытия списка.

# Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select.
# Далее можно найти любой вариант из списка с помощью метода select_by_value(value):

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")
# ищем элемент с текстом "Python"

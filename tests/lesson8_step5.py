from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']").send_keys("Anzh")
browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys("Khodzhaian")
browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("bla@bla.ru")

chooseFileButton = browser.find_element(By.XPATH, "//input[@id='file']")
submit = browser.find_element(By.XPATH, "//button[@type='submit']")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'd.txt')           # добавляем к этому пути имя файла
chooseFileButton.send_keys(file_path)

submit.click()

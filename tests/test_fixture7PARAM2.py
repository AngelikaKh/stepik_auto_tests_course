import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import math

mail = "a.123456@gmail.com"
password = "12345678"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('send_web', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_hidden_text(browser, send_web):
    link = f"https://stepik.org/lesson/{send_web}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "/html/body/header/nav/a[2]").click()
    browser.find_element(By.ID, "id_login_email").send_keys(mail)
    browser.find_element(By.ID, "id_login_password").send_keys(password)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)

    try:
        browser.implicitly_wait(10)
        button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        button_again.click()

    except NoSuchElementException:
        print('Кнопка "Решить снова" отсутствует')

    finally:
        time.sleep(5)
        input_answer = browser.find_element(By.TAG_NAME, 'textarea')
        input_answer.clear()

        answer = math.log(int(time.time()) - 0.034)
        answer_text = str(answer)

        input_answer.send_keys(answer_text)
        time.sleep(5)
        button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
        button_send.click()

        browser.implicitly_wait(10)
        answer_feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
        assert answer_feedback.text == "Correct!", "Wrong answer!"

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.fixture(scope="function")
# def browser(request):
# ...
#     options = OptionsChrome()
#     options.add_experimental_option(
#         'prefs', {'intl.accept_languages': user_language})
#
#     options_firefox = OptionsFirefox()
#     options_firefox.set_preference("intl.accept_languages", user_language)
# ...
#     if browser_name == "chrome":
# ...
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
# ...
#         browser = webdriver.Firefox(options=options_firefox)
# ...x(options=options)
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action = 'store', default = "chrome", help = "Choose browser: chrome or firefox")
    parser.addoption('--language', action = 'store', default = "ru", help = "Choose the language of interface")

@pytest.fixture(scope = "function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    if browser_name == "chrome":
        print("\n start chrome browser for test")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n start firefox browser for test")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))     
    browser.implicitly_wait(5)
    yield browser
    print("\n quit browser")
    browser.quit()


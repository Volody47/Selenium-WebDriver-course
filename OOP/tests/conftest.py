import pytest
from selenium import webdriver




def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, firefox or Ie")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # browser = webdriver.Firefox()
        browser = webdriver.Firefox(firefox_binary="C:\Program Files\Mozilla Firefox\\firefox.exe")
        browser.maximize_window()
    elif browser_name == "Ie":
        print("\nstart Ie browser for test..")
        browser = webdriver.Ie()
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or Ie")
    request.addfinalizer(browser.quit)
    print("\nquit browser..")
    return browser


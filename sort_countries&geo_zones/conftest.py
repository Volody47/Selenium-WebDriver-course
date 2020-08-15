import pytest
from selenium import webdriver




def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.set_window_size(1366, 800)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.set_window_size(1366, 800)
    elif browser_name == "Ie":
        print("\nstart Ie browser for test..")
        browser = webdriver.Ie()
        browser.set_window_size(1366, 800)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    request.addfinalizer(browser.quit)
    print("\nquit browser..")
    return browser


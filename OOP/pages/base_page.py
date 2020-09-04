from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

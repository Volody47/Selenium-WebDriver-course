from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture()
# def driver():
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_open_simple_page(driver):
    link = "https://www.google.com/"
    driver.get(link)

    #Fill out input
    search_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "q")))
    search_input.send_keys("selenium WebDriver")

    # Push search button
    push_search_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "btnK")))
    push_search_button.click()

    # Open first page
    open_first_page = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://www.selenium.dev/documentation/en/webdriver/']")))
    open_first_page.click()
    assert 'WebDriver' in driver.title

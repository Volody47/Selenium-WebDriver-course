from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_open_admin_login(driver):
    link = "http://localhost/litecart/admin/"
    driver.get(link)

    # Fill out input fields
    username_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "username")))
    username_input.send_keys("admin")

    password_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "password")))
    password_input.send_keys("admin")

    # Push login button
    button_login = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.NAME, "login")))
    button_login.click()

    # Expected value vs. Actual value
    assert "My Storet" == driver.title, "User not login"

import pytest

from pages.login_page import LoginPage
from data.testing_data import TestData
from utilities.logger import logGen

logger = logGen()

@pytest.mark.login
def test_login(initialize_driver):
    page = initialize_driver
    logger.info(f"Launching website")
    login_page = LoginPage(page)
    login_page.enter_username(TestData.username)
    login_page.enter_password(TestData.password)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Valid_login_TestData.png", full_page=True)
    actual_title = page.title()
    print('Actual Title:', actual_title)
    logger.info(f"Page Title {actual_title}")
    A= 5/0
    assert actual_title == TestData.Actual_Title

@pytest.mark.Invalidlogin
def test_invalidlogin(initialize_driver) -> None:
    page = initialize_driver
    login_page = LoginPage(page)
    login_page.enter_username(TestData.invalid_username)
    login_page.enter_password(TestData.invalid_password)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Invalid_login_TestData.png", full_page=True)







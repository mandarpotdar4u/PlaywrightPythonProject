import pytest

from pages.login_page import LoginPage
from data.testing_data import TestData
from utilities.logger import logGen


logger = logGen()


@pytest.mark.smoke
@pytest.mark.testdata
@pytest.mark.login
def test_login(initialize_driver):
    logger.info(f"Test_No:1 -> Valid Login_Test Data")
    # try:
    page = initialize_driver
    logger.info(f"Launching website")
    login_page = LoginPage(page)
    assert login_page.get_login_page_logo_text() == True
    login_page.login(TestData.username, TestData.password)
    page.screenshot(path="./screenshots/Valid_login_TestData.png", full_page=True)
    assert login_page.verify_title() == True
    # except AssertionError():
    # screenshot = page.screenshot(path="screenshot.png")
    # allure.attach.file("screenshot.png", name="Screenshot", attachment_type=AttachmentType.PNG)
    # raise

# finally:
# context.close()


@pytest.mark.smoke
@pytest.mark.testdata
@pytest.mark.Invalidlogin
def test_invalidlogin(initialize_driver):
    logger.info(f"Test_No:2 -> Invalid Login_Test Data")
    page = initialize_driver
    login_page = LoginPage(page)
    login_page.enter_username(TestData.invalid_username)
    login_page.enter_password(TestData.invalid_password)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Invalid_login_TestData.png", full_page=True)
    assert login_page.get_invalid_login_error_message() == True

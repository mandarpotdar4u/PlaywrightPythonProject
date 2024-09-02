import pytest

from pages.login_page import LoginPage
from utilities import readdatafromjson
from utilities.logger import logGen


logger = logGen()

@pytest.mark.login
def test_login(initialize_driver):
    page = initialize_driver
    logger.info(f"Launching website")
    login_page = LoginPage(page)
    login_page.enter_username(readdatafromjson.json_username)
    login_page.enter_password(readdatafromjson.json_password)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Valid_login_json.png", full_page=True)
    actual_title = page.title()
    print('Actual Title:', actual_title)
    logger.info(f"Json_Page Title {actual_title}")
    assert actual_title == readdatafromjson.json_Actual_Title

@pytest.mark.Invalidlogin
def test_invalidlogin( initialize_driver) -> None:
    page = initialize_driver
    login_page = LoginPage(page)
    login_page.enter_username(readdatafromjson.json_invalidusername)
    login_page.enter_password(readdatafromjson.json_invalidpassword)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Invalid_login_json.png", full_page=True)







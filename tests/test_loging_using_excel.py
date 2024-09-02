import pytest
import time
from pages.login_page import LoginPage
from utilities import excel_reader


@pytest.mark.parametrize("username,password",
                         excel_reader.get_valid_login_data_from_excel())
def test_valid_login_data_from_excel(initialize_driver, username, password):
    page = initialize_driver
    login_page = LoginPage(page)

    print("Logged in using username: " + username + " and password: " + password)

    login_page.enter_username(username)
    time.sleep(2)
    login_page.enter_password(password)
    # login_page.click_rememberme_button()
    time.sleep(2)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Valid_login_Excel.png", full_page=True)
    time.sleep(5)

    # Assertion validation through Excel Sheet
    actual_title = page.title()
    print('Page Excel Title:', actual_title)
    excel_Expected = excel_reader.get_valid_Page_Title_assertion_from_excel()
    assert actual_title == excel_Expected


@pytest.mark.parametrize("username,password",
                         excel_reader.get_invalid_login_data_from_excel())
def test_invalid_login_data_from_excel(initialize_driver, username, password):
    page = initialize_driver
    login_page = LoginPage(page)

    print("Logged in using username: " + username + " and password: " + password)
    login_page.enter_username(username)
    time.sleep(2)
    login_page.enter_password(password)
    # login_page.click_rememberme_button()
    time.sleep(2)
    login_page.click_Login_button()
    page.screenshot(path="./screenshots/Invalid_login_Excel.png", full_page=True)
    time.sleep(5)

# @pytest.mark.parametrize("username,password",
#                          excel_reader.get_invalid_login_data_from_excel('excel_fIles/testfile.xlsx', 'LoginTest'))
# def test_invalid_login_data_from_excel(initialize_driver, username, password):
#     page = initialize_driver
#     login_page = LoginPage(page)
#
#     print("Logged in using username: " + username + " and password: " + password)
#
#     login_page.enter_username(username)
#     time.sleep(2)
#     login_page.enter_password(password)
#     # login_page.click_rememberme_button()
#     time.sleep(2)
#     login_page.click_Login_button()
#     page.screenshot(path="./screenshots/Invalid_login_Excel.png", full_page=True)
#     time.sleep(5)

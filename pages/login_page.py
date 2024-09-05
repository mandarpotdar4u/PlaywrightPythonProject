from data.testing_data import TestData
from utilities.commonutilities import CommonUtilities
from utilities.logger import logGen
from utilities import readdatafromjson
from utilities import excel_reader
import time

logger = logGen()


class LoginPage(CommonUtilities):

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("//input[@id='user-name']")
        self.password_field = page.locator("//input[@id='password']")
        self.login_btn = page.locator("//input[@id='login-button']")
        self.invalid_login_error_message = page.locator("// div[@class ='error-message-container error']")
        self.login_page_title = page.locator("//div[contains(text(),'Swag Labs')]")

    """
     Below are the Login Page Methods 
     1. enter_username - It accept username as input parameter and return nothing
     2. enter_password - It accept password as input parameter and return nothing
     3. click_Login_button - It perform click action and return nothing
     4. login - It accept username,password as input parameter with click action and return nothing
    """

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.fill(username)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.fill(password)

    def click_Login_button(self):
        self.login_btn.click()

    def login(self, username, password):
        self.username_field.clear()
        self.username_field.fill(username)
        self.password_field.clear()
        self.password_field.fill(password)
        self.login_btn.click()

    # actual_title = page.title()
    # print('Actual Title:', actual_title)
    # logger.info(f"Page Title {actual_title}")
    # assert actual_title == TestData.Actual_Title

    """
     Below are the Login Page Assertion Methods 
     1. verify_title - It verify title from Test data file after login and return boolean - True/False
     2. get_login_page_logo_text - It verify login page logo title and return boolean - True/False
     3. get_invalid_login_error_message - It verify invalid login credential message and return boolean - True/False
     4. verify_title_json - It verify title from Json data file after login and return boolean - True/False
     5. verify_title_excel - It verify title from Excel data file after login and return boolean - True/False
    """

    def verify_title(self):
        actual_title = self.page.title()
        print('Page Actual Title:', actual_title)
        return actual_title == TestData.Actual_Title

    def get_login_page_logo_text(self):
        time.sleep(3)
        login_page_logo_text_locator = self.login_page_title.text_content()
        print('Page welcome_message_locator :', login_page_logo_text_locator)
        return login_page_logo_text_locator == TestData.Landing_Page_Title

    def get_invalid_login_error_message(self):
        invalid_login_cred_error_message = self.invalid_login_error_message.text_content()
        print('Invalid_login_error_message :', invalid_login_cred_error_message)
        return invalid_login_cred_error_message == TestData.invalid_login_cred_error_message

    def verify_title_json(self):
        actual_title = self.page.title()
        time.sleep(5)
        print('Page Actual Title:', actual_title)
        return actual_title == readdatafromjson.json_Actual_Title

    def verify_title_excel(self):
        actual_title = self.page.title()
        print('Page Actual Title:', actual_title)
        return actual_title == excel_reader.get_valid_Page_Title_assertion_from_excel()

    # ------------------> CommonUtilities Methods <-------------------

    def set_email_address(self, user_names):
        self.set_text(self.username_field, user_names)

    # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set_text(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_btn)


from utilities.commonutilities import CommonUtilities

class LoginPage(CommonUtilities):

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("//input[@id='user-name']")
        self.password_field = page.locator("//input[@id='password']")
        self.login_btn = page.locator("//input[@id='login-button']")
        self.invalid_error_message = page.locator("// div[@class ='error-message-container error']")

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.fill(username)

    def enter_password(self, passw):
        self.password_field.clear()
        self.password_field.fill(passw)

    def click_Login_button(self):
        self.login_btn.click()


    def set_email_address(self, user_names):
        self.set_text(self.username_field, user_names)

    # self.driver.find_element(self.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.set_text(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_btn)
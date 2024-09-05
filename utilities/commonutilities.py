from playwright.sync_api import Page


# Common Action methods
class CommonUtilities:
    # """It contains common methods"""

    def __init__(self, page):
        self.page = page

    def find(self, *locator):
        return self.page.locator(*locator)

    def click(self, *locator):
        self.find(*locator).click()

    # self.driver.find_element(*locator).click()

    def set_text(self, value, *locator):
        self.find(*locator).clear()
        self.find(*locator).fill(value)

    def get_text(self, *locator):
        return self.find(*locator).text

    def get_title(self):
        return self.page.title

    def Com_fill_element(self, locator: str, value: str):
        element = self.find(locator)
        element.fill(value)


from playwright.sync_api import Page

class LoginPage:
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test=error]"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        self.page.fill(self.USERNAME, username)

    def enter_password(self, password: str):
        self.page.fill(self.PASSWORD, password)

    def submit(self):
        self.page.click(self.LOGIN_BTN)

    def get_error(self) -> str:
        return self.page.text_content(self.ERROR_MSG)
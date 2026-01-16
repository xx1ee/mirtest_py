from ui.pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN = "#login"
    PASSWORD = "#password"
    SUBMIT = "#submit"

    def login(self, login: str, password: str):
        self.fill(self.LOGIN, login)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

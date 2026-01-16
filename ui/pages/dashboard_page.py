from ui.pages.base_page import BasePage

class DashboardPage(BasePage):
    USERNAME = "#username"

    def get_username(self) -> str:
        return self.page.text_content(self.USERNAME)

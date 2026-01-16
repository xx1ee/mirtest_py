from ui.pages.base_page import BasePage

class FormsPage(BasePage):
    NAME = "#name"
    EMAIL = "#email"
    SAVE = "#save"

    def submit_form(self, name: str, email: str):
        self.fill(self.NAME, name)
        self.fill(self.EMAIL, email)
        self.click(self.SAVE)

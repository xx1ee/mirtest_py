from playwright.sync_api import Page


class HomePage:
    HEADER = "h1"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://dummyjson.com/")

    def get_header_text(self) -> str:
        return self.page.text_content(self.HEADER)

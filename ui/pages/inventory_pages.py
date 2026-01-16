from playwright.sync_api import Page


class InventoryPage:
    INVENTORY_CONTAINER = ".inventory_list"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def is_opened(self) -> bool:
        return self.page.is_visible(self.INVENTORY_CONTAINER)

# ui/pages/dashboard_page.py
class DashboardPage:
    def __init__(self, page):
        self.page = page

    def is_opened(self) -> bool:
        return self.page.locator("h6:has-text('Dashboard')").is_visible()

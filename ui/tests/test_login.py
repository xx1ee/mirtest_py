from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage
from conf.settings import settings

def test_success_login(page):
    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open(f"{settings.base_url_ui}/login")
    login.login("admin", "admin123")

    assert dashboard.get_username() == "admin"

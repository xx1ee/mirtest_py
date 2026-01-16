import pytest
from playwright.sync_api import Page, sync_playwright

from api.shop_api import ShopAPI
from ui.pages.login_page import LoginPage
import pytest
from api.jwt_provider import JWTProvider


@pytest.fixture
def login_page(page: Page):
    from ui.pages.login_page import LoginPage
    return LoginPage(page)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для API"""
    return ShopAPI()

@pytest.fixture(scope="function")
def page():
    """Playwright Page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=True для CI
        page = browser.new_page()
        yield page
        page.close()
        browser.close()

@pytest.fixture(scope="session")
def jwt_token():
    return JWTProvider.generate(
        user_id=123,
        role="admin"
    )


@pytest.fixture(scope="session")
def api_auth_token():
    return "mocked-jwt-token-123"



@pytest.fixture
def authenticated_page(page, jwt_token):
    page.goto("https://dummyjson.com")

    # создаём cookie
    page.context.add_cookies([{
        "name": "token",
        "value": jwt_token,
        "domain": "dummyjson.com",
        "path": "/"
    }])

    return page




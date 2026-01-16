import pytest
from playwright.sync_api import Page
from conf.settings import settings
from api.client import APIClient

@pytest.fixture
def page(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.set_default_timeout(settings.timeout)
    yield page

@pytest.fixture
def api_client():
    return APIClient(settings.base_url_api)

from ui.pages.forms_page import FormsPage

def test_submit_form(page):
    form = FormsPage(page)

    page.goto("https://example.com/forms")
    form.submit_form("Ivan", "ivan@test.ru")

    assert page.is_visible(".success")

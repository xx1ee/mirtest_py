def test_navigation_to_forms(page):
    page.goto("https://example.com/dashboard")
    page.click("#forms-link")

    assert page.url.endswith("/forms")

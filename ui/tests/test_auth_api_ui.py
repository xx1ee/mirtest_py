def test_open_cart_as_authenticated_user(authenticated_page):
    page = authenticated_page
    page.goto("https://dummyjson.com/carts/1")

    # ждём появления таблицы товаров или заголовка корзины
    page.locator("text=Products").wait_for(state="visible", timeout=5000)

    # проверяем, что таблица/список продуктов видим
    assert page.locator("text=Products").is_visible()

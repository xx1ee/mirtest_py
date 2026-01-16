
def test_negative_without_password(login_page):
    # Arrange
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("")
    login_page.submit()

    error = login_page.get_error()
    assert error == "Epic sadface: Password is required"

def test_negative_without_login(login_page):
    login_page.open()
    login_page.enter_username("")
    login_page.enter_password("secret_sauce")
    login_page.submit()

    error = login_page.get_error()
    assert error == "Epic sadface: Username is required"

def test_negative_invalid_login(login_page):
    login_page.open()
    login_page.enter_username("login")
    login_page.enter_password("secret_sauce")
    login_page.submit()

    error = login_page.get_error()
    assert error == "Epic sadface: Username and password do not match any user in this service"

def test_positive_login(login_page, page):
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.submit()

    assert page.url == "https://www.saucedemo.com/inventory.html"

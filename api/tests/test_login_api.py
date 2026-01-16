def test_login_api_success(api_auth_token):
    assert isinstance(api_auth_token, str)
    assert len(api_auth_token) > 0

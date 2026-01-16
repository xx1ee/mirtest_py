from api.models import Cart
import pytest
from api.shop_api import ShopAPI


def test_cart_total_depends_on_quantity():
    api = ShopAPI()

    response = api.create_cart(
        user_id=1,
        products=[
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 1},
        ]
    )

    cart = Cart.model_validate(response.json())

    assert cart.total > 0
    assert len(cart.products) == 2

    calculated = sum(p.price * p.quantity for p in cart.products)
    assert calculated == cart.total


def test_cannot_create_cart_without_products():
    api = ShopAPI()

    with pytest.raises(ValueError):
        api.create_cart(user_id=1, products=[])

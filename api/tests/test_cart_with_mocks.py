import responses
import pytest
from api.shop_api import ShopAPI
from api.models import Cart, CartProduct


@responses.activate
def test_create_cart_mocked_response():
    responses.add(
        method=responses.POST,
        url="https://dummyjson.com/carts/add",
        json={
            "id": 123,
            "userId": 1,
            "total": 300,
            "discountedTotal": 270,
            "products": [
                {
                    "id": 1,
                    "title": "Phone",
                    "price": 100,
                    "quantity": 3,
                    "total": 300
                }
            ]
        },
        status=200
    )

    api = ShopAPI()
    response = api.create_cart(
        user_id=1,
        products=[{"id": 1, "quantity": 3}]
    )

    cart = Cart.model_validate(response.json())

    assert cart.id == 123
    assert cart.total == 300
    assert cart.discountedTotal == 270

@responses.activate
def test_api_returns_500_error():
    responses.add(
        responses.POST,
        "https://dummyjson.com/carts/add",
        json={"error": "Internal Server Error"},
        status=500
    )

    api = ShopAPI()

    try:
        api.create_cart(
            user_id=1,
            products=[{"id": 1, "quantity": 1}]
        )
    except Exception as e:
        assert "500" in str(e)



@responses.activate
def test_create_cart_with_discount_and_multiple_products():
    # 🔹 Мокаем POST-запрос
    responses.add(
        method=responses.POST,
        url="https://dummyjson.com/carts/add",
        json={
            "id": 123,
            "userId": 1,
            "total": 350.0,
            "discountedTotal": 315.0,
            "products": [
                {"id": 1, "title": "Phone", "price": 100.0, "quantity": 2, "total": 200.0},
                {"id": 2, "title": "Headphones", "price": 150.0, "quantity": 1, "total": 150.0}
            ]
        },
        status=200
    )

    api = ShopAPI()
    response = api.create_cart(
        user_id=1,
        products=[
            {"id": 1, "quantity": 2},
            {"id": 2, "quantity": 1}
        ]
    )

    cart = Cart.model_validate(response.json())

    # 🔹 Проверяем бизнес-логику
    assert cart.id == 123
    assert cart.userId == 1
    assert len(cart.products) == 2
    assert cart.total == 350.0
    assert cart.discountedTotal == 315.0

    # 🔹 Проверяем, что сумма продуктов совпадает с total
    calculated_total = sum(p.price * p.quantity for p in cart.products)
    assert abs(calculated_total - cart.total) < 0.01

    # 🔹 Проверяем скидку
    discount_percentage = (cart.total - cart.discountedTotal) / cart.total * 100
    assert discount_percentage == 10.0  # 10% скидка


@responses.activate
def test_cannot_add_negative_quantity():
    responses.add(
        method=responses.POST,
        url="https://dummyjson.com/carts/add",
        json={"error": "Quantity must be positive"},
        status=400
    )

    api = ShopAPI()

    with pytest.raises(Exception) as excinfo:
        api.create_cart(user_id=1, products=[{"id": 1, "quantity": -2}])

    # 🔹 Проверяем код
    assert excinfo.value.response.status_code == 400

    # 🔹 Проверяем тело ответа
    assert excinfo.value.response.json()["error"] == "Quantity must be positive"


@responses.activate
def test_cart_total_recalculation_after_removal():
    # 🔹 Сценарий: сначала корзина с 2 товарами
    responses.add(
        method=responses.POST,
        url="https://dummyjson.com/carts/add",
        json={
            "id": 200,
            "userId": 1,
            "total": 250.0,
            "discountedTotal": 225.0,
            "products": [
                {"id": 1, "title": "Keyboard", "price": 100.0, "quantity": 1, "total": 100.0},
                {"id": 2, "title": "Mouse", "price": 150.0, "quantity": 1, "total": 150.0}
            ]
        },
        status=200
    )

    api = ShopAPI()
    response = api.create_cart(
        user_id=1,
        products=[{"id": 1, "quantity": 1}, {"id": 2, "quantity": 1}]
    )
    cart = Cart.model_validate(response.json())

    # 🔹 Проверка суммы
    assert abs(cart.total - 250.0) < 0.01
    assert abs(cart.discountedTotal - 225.0) < 0.01

    # 🔹 Теперь представим, что удаляем Mouse (через мок API)
    responses.add(
        method=responses.POST,
        url="https://dummyjson.com/carts/add",
        json={
            "id": 200,
            "userId": 1,
            "total": 100.0,
            "discountedTotal": 90.0,
            "products": [
                {"id": 1, "title": "Keyboard", "price": 100.0, "quantity": 1, "total": 100.0},
            ]
        },
        status=200
    )

    response_after_removal = api.create_cart(user_id=1, products=[{"id": 1, "quantity": 1}])
    cart_after = Cart.model_validate(response_after_removal.json())

    # 🔹 Проверяем пересчёт total и discountedTotal
    assert cart_after.total == 100.0
    assert cart_after.discountedTotal == 90.0

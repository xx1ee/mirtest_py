from pydantic import BaseModel
from typing import List, Optional

class LoginResponse(BaseModel):
    token: str
    user_id: int




class CartProduct(BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    total: float


class Cart(BaseModel):
    id: int
    userId: int
    total: float
    discountedTotal: int
    products: List[CartProduct]


from pydantic import BaseModel
from datetime import datetime
from typing import List

class OrderBase(BaseModel):
    product_id: int
    customer_name: str
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: datetime
    class Config: orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    orders: List[Order] = []
    class Config: orm_mode = True
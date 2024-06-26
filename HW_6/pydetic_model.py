from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    product_id: int
    product_name: str
    description : str
    price: float


class ProductIn(BaseModel):
    product_name: str
    description : str
    price: float


class Order(BaseModel):
    order_id: int
    product_id: int
    user_id: int


class OrderIn(BaseModel):
    product_id: int
    user_id: int


class User(BaseModel):
    user_id: int
    username: str
    surname: str
    email: str
    password: str


class UserInPassword(BaseModel):
    username: str
    surname: str
    email: str
    password: str


class UserIn(BaseModel):
    username: str
    surname: str
    email: str



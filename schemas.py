from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date


class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None

class UserGetId(BaseModel):
    id: int
    email: str
    name: str
    class Config:
        orm_mode = True
    # Спросить, нужно ли убирать ограничения на словари?

class UserDelete(BaseModel):
    id: int

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[int] = None

class ProductGetId(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    in_stock: int
    class Config:
        orm_mode = True

class ProductDelete(BaseModel):
    id: int

class OrderCreate(BaseModel):
    product_ids: List[int]
    customer_name: str
    shipping_address: str
    note: Optional[str] = None
    date_of_creation: date
    date_of_shipping: str

class OrderUpdate(BaseModel):
    product_ids: Optional[List[int]] = None
    customer_name: Optional[str] = None
    shipping_address: Optional[str] = None
    note: Optional[str] = None

class OrderGetId(BaseModel):
    id: int
    user_id: int
    product_ids: List[int]
    note: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class OrderDelete(BaseModel):
    id: int
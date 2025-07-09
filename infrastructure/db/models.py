from time import timezone
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, ARRAY, DateTime, Float
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Integer
from datetime import datetime
from sqlalchemy import func

class Base(DeclarativeBase):
    pass

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_ids: Mapped[List[int]] = mapped_column(ARRAY(Integer))
    customer_name: Mapped[str] = mapped_column(String(100))
    shipping_address: Mapped[str] = mapped_column(String(500))
    note: Mapped[str] = mapped_column(String(1000))
    date_of_creation: Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default= func.now())
    date_of_shipping = Mapped[str] = mapped_column(String(100))

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float())

class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100))


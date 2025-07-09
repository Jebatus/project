from abc import ABC
from infrastructure.db.models import Product
from application.interfaces.product_dao import ProductDAOInterface
from schemas import ProductCreate, ProductGetId

class ProductDaoImpl(ProductDAOInterface, ABC):
    def __init__(self, session):
        self.session = session
    def product_create(self, product: ProductCreate):
        product_create = Product(name = product.name, price = product.price)
        self.session.add(product_create)
        self.session.commit()
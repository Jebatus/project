from application.interfaces.user_service import UserServiceInterface
from schemas import UserCreate

class ProductServiceImplementation(ProductServiceInterface):
    def create_product(self, product: ProductCreate):
        self.dao.create_product(product)
from abc import ABC, abstractmethod
from typing import Optional, List
from schemas import ProductCreate, ProductUpdate, ProductGetId

class ProductDAOInterface(ABC):
    @abstractmethod
    async def get_by_id(self, product_id: int) -> Optional[ProductGetId]:
        pass

    @abstractmethod
    async def create_product(self, product: ProductCreate) -> ProductGetId:
        pass

    @abstractmethod
    async def update_product(self, product_id: int, product: ProductUpdate) -> ProductGetId:
        pass

    @abstractmethod
    async def delete_product(self, product_id: int) -> None:
        pass

    @abstractmethod
    async def list_products(self) -> List[ProductGetId]:
        pass
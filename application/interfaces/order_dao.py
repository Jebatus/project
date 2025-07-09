from abc import ABC, abstractmethod
from typing import Optional, List
from schemas import OrderCreate, OrderUpdate, OrderGetId

class OrderDAOInterface(ABC):
    @abstractmethod
    async def get_by_id(self, order_id: int) -> Optional[OrderGetId]:
        pass

    @abstractmethod
    async def create_order(self, order: OrderCreate) -> OrderGetId:
        pass

    @abstractmethod
    async def update_order(self, order_id: int, order: OrderUpdate) -> OrderGetId:
        pass

    @abstractmethod
    async def delete_order(self, order_id: int) -> None:
        pass

    @abstractmethod
    async def list_orders(self) -> List[OrderGetId]:
        pass
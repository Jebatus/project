#from abc import ABC, abstractmethod

#class UserDAOInterface(ABC):
#    @abstractmethod
#    async def get_by_id(self, user_id: int):
#        pass

from abc import ABC, abstractmethod
from typing import Optional, List
from schemas import UserCreate, UserUpdate, UserGetId

class UserDAOInterface(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: int) -> Optional[UserGetId]:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> Optional[UserGetId]:
        pass

    @abstractmethod
    async def create_user(self, user: UserCreate) -> UserGetId:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user: UserUpdate) -> UserGetId:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    async def list_users(self) -> List[UserGetId]:
        pass
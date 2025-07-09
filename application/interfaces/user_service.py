from application.interfaces.user_dao import UserDAOInterface
from abc import ABC, abstractmethod
from schemas import UserCreate

class UserServiceInterface(ABC):
    def __init__(self, dao: UserDAOInterface):
        self.dao = dao
    @abstractmethod
    def create_user(self, user: UserCreate):
        pass



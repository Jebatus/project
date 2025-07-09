from application.interfaces.user_service import UserServiceInterface
from schemas import UserCreate

class UserServiceImplementation(UserServiceInterface):
    def create_user(self, user: UserCreate):
        self.dao.create_user(user)

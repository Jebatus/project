from abc import ABC
from infrastructure.db.models import User
from application.interfaces.user_dao import UserDAOInterface
from schemas import UserCreate, UserGetId

class UserDaoImpl(UserDAOInterface, ABC):
    def __init__(self, session):
        self.session = session
    def user_create(self, user: UserCreate):
        user_create = User(name = user.name, password = user.password, email = user.email)
        self.session.add(user_create)
        self.session.commit()
from dishka import make_async_container, Provider, provide, Scope
from application.interfaces.order_dao import OrderDAOInterface
from application.interfaces.product_dao import ProductDAOInterface
from application.interfaces.user_dao import UserDAOInterface
#from application.interfaces.filters_service import
#from application.interfaces.order_service import
from application.interfaces.user_service import UserServiceInterface
from infrastructure.dao.user_dao_impl import UserDaoImpl
from infrastructure.dao.order_dao_impl import OrderDaoImpl
from infrastructure.dao.product_dao_impl import ProductDaoImpl
#from infrastructure.services.filters_service_impl import
#from infrastructure.services.order_service_impl import
#from infrastructure.services.product_service_impl import
from infrastructure.services.user_service_impl import UserServiceImplementation
from dishka import make_container
from infrastructure.db.database import SessionLocal

service_provider = Provider(scope=Scope.REQUEST)
service_provider.provide(UserServiceImplementation, provides=UserServiceInterface)
service_provider.provide(UserDaoImpl, provides=UserDAOInterface)

class ConnectionProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_db_session(self):
        session = SessionLocal()
        try:
            yield session
        finally:
            session.close()

def create_container():
    return make_container(service_provider, ConnectionProvider())


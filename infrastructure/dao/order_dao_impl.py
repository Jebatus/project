from abc import ABC
from infrastructure.db.models import Order

from application.interfaces.order_dao import OrderDAOInterface
from schemas import OrderCreate, OrderGetId

class OrderDaoImpl(OrderDAOInterface, ABC):
    def __init__(self, session):
        self.session = session
    def create_order(self, order: OrderCreate):
        order_create = Order(product_ids = order.product_ids, customer_name = order.customer_name, shipping_adress = order.shipping_address, note = order.note, date_of_creation = order.date_of_creation, date_of_shipping = order.date_of_shipping)
        self.session.add(order_create)
        self.session.commit()




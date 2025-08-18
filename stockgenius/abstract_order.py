from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    
    def __eq__(self, other):
        if isinstance(other, OrderStatus):
            return self.value == other.value
        return False

class AbstractOrder(ABC):
    """Abstract base class for all types of orders."""
    
    def __init__(self, order_id: str, products: list):
        self.__order_id = order_id
        self.__products = products
        self.__date = datetime.now()
        self.__status = OrderStatus.PENDING

    @property
    def order_id(self):
        return self.__order_id

    @property
    def products(self):
        return self.__products

    @property
    def date(self):
        return self.__date

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status: OrderStatus):
        self.__status = new_status

    @abstractmethod
    def calculate_total(self) -> float:
        """Calculate the total price of the order."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """String representation of the order."""
        pass

    def list_products(self):
        """
        Lists all products in the order.
        
        Returns:
            str: Formatted string containing all products in the order.
        """
        ret = "Products in the order:\nProduct ID | Name | Quantity | Price\n"
        ret = "-"*80 + "\n" + ret + "-"*80 + "\n"
        for product in self.products:
            ret += f"{product.product_id} | {product.name} | {product.quantity} | {product.price}\n{'-'*80}\n"
        return ret
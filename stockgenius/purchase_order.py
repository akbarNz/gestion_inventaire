from datetime import datetime, timedelta
from stockgenius.abstract_order import AbstractOrder, OrderStatus
from stockgenius.supplier import Supplier

class PurchaseOrder(AbstractOrder):
    """Represents an order to a supplier."""

    def __init__(self, order_id: str, products: list, supplier: Supplier):
        super().__init__(order_id, products)
        self.__supplier = supplier
        self.__expected_delivery = datetime.now() + timedelta(days=7)

    @property
    def supplier(self):
        return self.__supplier

    @property
    def expected_delivery(self):
        return self.__expected_delivery

    @expected_delivery.setter
    def expected_delivery(self, date: datetime):
        self.__expected_delivery = date

    def calculate_total(self) -> float:
        """Calculate total without VAT."""
        return sum(product.price * product.quantity for product in self.products)

    def __str__(self) -> str:
        return f"Purchase Order({self.order_id}, {self.supplier.name}, {len(self.products)} products, Status: {self.status.value})"
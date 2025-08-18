from stockgenius.product import Product
from stockgenius.abstract_order import AbstractOrder, OrderStatus

class SaleOrder(AbstractOrder):
    """
    Represents a customer order containing multiple products.

    Attributes:
        order_id (str): The unique identifier for the order.
        products (list): A list of Product objects in the order.
        total_price (float): The total price of the order.
    """

    def __init__(self, order_id, products):
        """
        Initializes a new SaleOrder instance.

        Args:
            order_id (str): The unique identifier for the order.
            products (list): A list of Product objects in the order.
        """
        super().__init__(order_id, products)
        self.__total_price = self.calculate_total()

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, new_total_price):
        self.__total_price = new_total_price

    def calculate_total(self):
        """
        Calculates the total price of the order including VAT.

        Returns:
            float: The total price of the order.
        """
        total = 0
        for product in self.products:
            total += product.calculate_price_with_vat()
        return total

    def add_product(self, product):
        """
        Adds a product to the order.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)
        self.total_price = self.calculate_total()

    def remove_product(self, product):
        """
        Removes a product from the order.

        Args:
            product (Product): the product to remove.
        """
        self.products.remove(product)
        self.total_price = self.calculate_total()

    def search_product_by_id(self, product_id):
        """Search a product by its product_id.
        
        Args:
            product_id (str): The ID of the product to search.
        
        Returns:
            the product (Product) if found None otherwise.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def __str__(self):
        """Returns a string representation of the order."""
        return f"{'-'*80}\nOrder ID: {self.order_id}\nStatus: {self.status.value}\nTotal price: {self.total_price}\nProducts: {len(self.products)}\n{'-'*80}"
class Product:
    """
    Represents an item in the inventory.

    Attributes:
        product_id (str): The unique identifier for the product.
        name (str): The name of the product.
        quantity (int): The quantity of the product in stock.
        price (float): The price of the product.
        category (Category): The category to which the product belongs.
    """

    def __init__(self, product_id, name, quantity, price, category):
        """
        Initializes a new Product instance.

        Args:
            product_id (str): The unique identifier for the product.
            name (str): The name of the product.
            quantity (int): The quantity of the product in stock.
            price (float): The price of the product.
            category (Category): The category to which the product belongs.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def get_price(self):
        """
        Returns the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.price

    def set_price(self, new_price):
        """
        Updates the price of the product.

        Args:
            new_price (float): The new price of the product.
        """
        self.price = new_price

    def get_name(self):
        """
        Returns the name of the product.

        Returns:
            str: The name of the product.
        """
        return self.name

    def set_name(self, new_name):
        """
        Updates the name of the product.

        Args:
            new_name (str): The new name of the product.
        """
        self.name = new_name

    def set_quantity(self, new_quantity):
        """
        Updates the quantity of the product.

        Args:
            new_quantity (int): The new quantity of the product.
        """
        self.quantity = new_quantity

    def __str__(self):
        """
        Returns a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        return f"Product({self.product_id}, {self.name}, {self.quantity}, {self.price}, {self.category.name})"

    def calculate_price_with_vat(self):
        """
        Calculates the price of the product including VAT.

        Returns:
            float: The price of the product including VAT.
        """
        return self.price * (1 + self.category.vat)
class Order:
    """
    Represents an order containing multiple products.

    Attributes:
        order_id (str): The unique identifier for the order.
        products (list): A list of Product objects in the order.
        total_price (float): The total price of the order.
    """

    def __init__(self, order_id, products):
        """
        Initializes a new Order instance.

        Args:
            order_id (str): The unique identifier for the order.
            products (list): A list of Product objects in the order.
        """
        self.order_id = order_id
        self.products = products
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        """
        Calculates the total price of the order.

        Returns:
            float: The total price of the order.
        """
        return sum(product.price for product in self.products)

    def add_product(self, product):
        """
        Adds a product to the order.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)
        self.total_price = self.calculate_total_price()

    def remove_product(self, product_id):
        """
        Removes a product from the order by its ID.

        Args:
            product_id (str): The ID of the product to remove.
        """
        self.products = [p for p in self.products if p.product_id != product_id]
        self.total_price = self.calculate_total_price()

    def get_products(self):
        """
        Retrieves all products in the order.

        Returns:
            list: A list of all products in the order.
        """
        return self.products

    def get_total_price(self):
        """
        Retrieves the total price of the order.

        Returns:
            float: The total price of the order.
        """
        return self.total_price

    def get_order_id(self):
        """
        Retrieves the ID of the order.

        Returns:
            str: The ID of the order.
        """
        return self.order_id
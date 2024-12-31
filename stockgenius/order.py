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
        self.__order_id = order_id
        self.__products = products
        self.__total_price = self.calculate_total_price()

    # GETTERS AND SETTERS
    @property
    def products(self):
        return self.__products

    @property
    def total_price(self):
        return self.__total_price

    @property
    def order_id(self):
        return self.__order_id
    
    # METHODS
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
        tmp = self._seach_product_by_id(product_id)

        if tmp:
            self.products.remove(tmp)

    def _seach_product_by_id(self, product_id):
        """Search a product by its product_id.
        
        Args:
            product_id (str): The ID of the product to search.
        
        Returns:
            the product (Product) if found None otherwise.
        """
        i = 0
        found = False
        tmp = None
        while not found and i < len(self.products):
            if self.products[i].product_id == product_id:
                tmp = self.products[i]
                found = True
            i += 1

        return tmp
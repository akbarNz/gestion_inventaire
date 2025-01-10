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
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__category = category

    # GETTER AND SETTER
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):

        if new_price > 0:
            self.__price = new_price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        if isinstance(new_quantity, int):
            self.__quantity = new_quantity
        else:
            raise TypeError(f"type of new_quantity must be int. {type(new_quantity)} not supported")

    @property
    def category(self):
        return self.__category
    
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
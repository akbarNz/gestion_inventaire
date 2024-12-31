class Inventory:
    """
    Manages the collection of products, categories, and orders.

    Attributes:
        products (list): A list of Product objects.
        categories (list): A list of Category objects.
        orders (list): A list of Order objects.
    """

    def __init__(self):
        """
        Initializes a new Inventory instance.
        """
        self.products = []
        self.categories = []
        self.orders = []

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product_id):
        """
        Removes a product from the inventory by its ID.

        Args:
            product_id (str): The ID of the product to remove.
        """
        self.products = [p for p in self.products if p.product_id != product_id]

    def get_product_by_id(self, product_id):
        """
        Retrieves a product by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def get_products_by_category(self, category_name):
        """
        Retrieves products by their category.

        Args:
            category_name (str): The name of the category.

        Returns:
            list: A list of products in the specified category.
        """
        return [p for p in self.products if p.category.name == category_name]

    def search_products_by_name(self, name):
        """
        Searches for products by their name.

        Args:
            name (str): The name of the product to search for.

        Returns:
            list: A list of products that match the search criteria.
        """
        return [p for p in self.products if name.lower() in p.name.lower()]

    def search_products_by_price_range(self, min_price, max_price):
        """
        Searches for products within a specified price range.

        Args:
            min_price (float): The minimum price.
            max_price (float): The maximum price.

        Returns:
            list: A list of products within the specified price range.
        """
        return [p for p in self.products if min_price <= p.price <= max_price]

    def update_product_price(self, product_id, new_price):
        """
        Updates the price of a product.

        Args:
            product_id (str): The ID of the product to update.
            new_price (float): The new price of the product.
        """
        product = self.get_product_by_id(product_id)
        if product:
            product.set_price(new_price)

    def update_category_vat(self, category_name, new_vat):
        """
        Updates the VAT rate for a category.

        Args:
            category_name (str): The name of the category to update.
            new_vat (float): The new VAT rate for the category.
        """
        for category in self.categories:
            if category.name == category_name:
                category.set_vat(new_vat)

    def calculate_product_price_with_vat(self, product_id):
        """
        Calculates the price of a product including VAT.

        Args:
            product_id (str): The ID of the product.

        Returns:
            float: The price of the product including VAT.
        """
        product = self.get_product_by_id(product_id)
        if product:
            return product.calculate_price_with_vat()
        return None

    def generate_sales_summary(self):
        """
        Generates a summary of sales.

        Returns:
            str: A summary of sales.
        """
        summary = "Sales Summary:\n"
        for order in self.orders:
            summary += f"Order ID: {order.order_id}, Total Price: {order.total_price}\n"
        return summary

    def generate_inventory_report(self):
        """
        Generates a report of the inventory.

        Returns:
            str: A report of the inventory.
        """
        report = "Inventory Report:\n"
        for product in self.products:
            report += str(product) + "\n"
        return report

    def get_products(self):
        """
        Retrieves all products in the inventory.

        Returns:
            list: A list of all products in the inventory.
        """
        return self.products

    def get_categories(self):
        """
        Retrieves all categories in the inventory.

        Returns:
            list: A list of all categories in the inventory.
        """
        return self.categories

    def add_new_order(self, order):
        """
        Adds a new order to the inventory.

        Args:
            order (Order): The order to add.
        """
        self.orders.append(order)

    def search_order(self, order_id):
        """
        Searches for an order by its ID.

        Args:
            order_id (str): The ID of the order to search for.

        Returns:
            Order: The order with the specified ID.
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def remove_order(self, order_id):
        """
        Removes an order from the inventory by its ID.

        Args:
            order_id (str): The ID of the order to remove.
        """
        self.orders = [o for o in self.orders if o.order_id != order_id]
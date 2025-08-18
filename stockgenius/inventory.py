from stockgenius.category import Category
from stockgenius.product import Product
from stockgenius.sale_order import SaleOrder  # Changed from Order
from stockgenius.purchase_order import PurchaseOrder
from stockgenius.supplier import Supplier

class Inventory:
    """
    Manages the collection of products, categories, orders, and suppliers.

    Attributes:
        products (list): A list of Product objects.
        categories (list): A list of Category objects.
        orders (list): A list of Order objects.
        suppliers (list): A list of Supplier objects.
    """

    def __init__(self):
        """
        Initializes a new Inventory instance.
        """
        self.__products = []
        self.__categories = []
        self.__orders = []
        self.__suppliers = []
        self.__sale_orders = []
        self.__purchase_orders = []

    # GETTERS AND SETTERS

    @property
    def products(self):
        return self.__products

    @property
    def categories(self):
        return self.__categories
    
    @property
    def orders(self):
        return self.__orders
    
    @property
    def suppliers(self):
        return self.__suppliers
    
    @property
    def sale_orders(self):
        return self.__sale_orders

    @property
    def purchase_orders(self):
        return self.__purchase_orders
    
    # BUILTINS REDEFINED
    def __str__(self):
        return f"{'-'*80}\nInventory Report\nTotal products: {len(self.products)}\nOrders: {len(self.orders)}\nCategories: {[c.name for c in self.categories]}\n{'-'*80}"
    # PRINTING
    def list_products(self):
        """
        Lists all products in the inventory and their prices. 
        """
        ret = "\nProducts in the inventory:\nProduct ID | Name | Price\n"
        ret = "-"*80 + ret +"-"*80 + "\n"
        for product in self.products:
            ret += f"{product.product_id} | {product.name} | {product.price}\n {'-'*80}\n"
        return ret
    # METHODS

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)
    
    def add_category(self, category):
        """
        Adds a category to the inventory.

        Args:
            category (Category): The category to add.
        """
        self.categories.append(category)
    
    def remove_category(self, category_name):
        """
        Removes a category from the inventory by its name.

        Args:
            category_name (str): The name of the category to remove.
        """
        tmp = self.search_category_by_name(category_name)

        if tmp:
            self.categories.remove(tmp)
        
    
    def remove_product(self, product):
        """
        Removes a product from the inventory.

        Args:
            product (Product): The ID of the product to remove.
        """
        self.products.remove(product)

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

    def search_category_by_name(self, name):
        """Search a category by its name.
        
        Args:
            name (str): the name of the category

        Returns:
            a category (Category) if found, None otherwise.    
        """
        i = 0
        found = False
        tmp = None
        while not found and i < len(self.categories):
            if name == self.categories[i].name:
                found = True
                tmp = self.categories[i]
                
            i += 1
        return tmp

    def search_products_by_category_name(self, category_name):
        """
        Searches for products by their category name.

        Args:
            category_name (str): The name of the category to search for.

        Returns:
            list: A list of products that match the search criteria.
        """
        return [p for p in self.products if p.category.name == category_name]
    
    def update_product_price(self, product_id, new_price):
        """
        Updates the price of a product.

        Args:
            product_id (str): The ID of the product to update.
            new_price (float): The new price of the product.
        """
        product = self.get_product_by_id(product_id)
        if product:
            product.price = new_price

    def update_category_vat(self, category_name, new_vat):
        """
        Updates the VAT rate for a category.

        Args:
            category_name (str): The name of the category to update.
            new_vat (float): The new VAT rate for the category.
        """
        for category in self.categories:
            if category.name == category_name:
                category.vat = new_vat

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

    def remove_order(self, order_id):
        """
        Removes an order from the inventory by its ID.

        Args:
            order_id (str): The ID of the order to remove.
        """
        tmp = self.get_order_by_id(order_id)

        if tmp:
            self.orders.remove(tmp)
    
    def get_order_by_id(self, order_id):
        """Search an order by its order_id.

        Args:
            order_id (str): The ID of the order to search
        
        Returns:
            order (Order) if found, None otherwise.
        """

        i = 0
        found = False
        tmp = None

        while not found and i < len(self.orders):
            if self.orders[i].order_id == order_id:
                tmp = self.orders[i]
                found = True
            i += 1
        
        return tmp

    def add_supplier(self, supplier):
        """Add a supplier to the inventory."""
        if supplier not in self.__suppliers:
            self.__suppliers.append(supplier)

    def remove_supplier(self, supplier_id):
        """Remove a supplier from the inventory."""
        self.__suppliers = [s for s in self.__suppliers if s.supplier_id != supplier_id]

    def get_supplier_by_id(self, supplier_id):
        """Get a supplier by their ID."""
        for supplier in self.__suppliers:
            if supplier.supplier_id == supplier_id:
                return supplier
        return None

    def get_suppliers_by_product(self, product_id):
        """Get all suppliers that supply a specific product."""
        return [s for s in self.__suppliers if any(p.product_id == product_id for p in s.products)]

    def list_suppliers(self):
        """List all suppliers in the inventory."""
        return "\n".join(str(supplier) for supplier in self.__suppliers)

    def add_sale_order(self, order):
        """Add a sale order to the inventory."""
        if order not in self.__sale_orders:
            self.__sale_orders.append(order)

    def add_purchase_order(self, order):
        """Add a purchase order to the inventory."""
        if order not in self.__purchase_orders:
            self.__purchase_orders.append(order)
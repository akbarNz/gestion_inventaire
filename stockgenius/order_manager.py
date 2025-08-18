from datetime import datetime
from stockgenius.inventory import Inventory
from stockgenius.purchase_order import PurchaseOrder
from stockgenius.product import Product

class OrderManager:
    """Manages automated purchase orders and inventory monitoring."""

    def __init__(self, inventory: Inventory):
        self.inventory = inventory
        self.__last_check = datetime.now()

    def check_stock_levels(self):
        """Check stock levels and generate purchase orders if needed."""
        orders_to_create = {}  # supplier_id: [products]
        
        for product in self.inventory.products:
            if product.quantity <= product.reorder_point:
                if product.supplier.supplier_id not in orders_to_create:
                    orders_to_create[product.supplier.supplier_id] = []
                
                # Calculate order quantity
                order_quantity = product.optimal_stock - product.quantity
                product_copy = Product(
                    product.product_id,
                    product.name,
                    order_quantity,
                    product.price,
                    product.category,
                    product.supplier
                )
                orders_to_create[product.supplier.supplier_id].append(product_copy)

        # Create purchase orders
        for supplier_id, products in orders_to_create.items():
            supplier = self.inventory.get_supplier_by_id(supplier_id)
            if supplier:
                order_id = f"PO{datetime.now().strftime('%Y%m%d%H%M%S')}"
                purchase_order = PurchaseOrder(order_id, products, supplier)
                self.inventory.add_purchase_order(purchase_order)

        self.__last_check = datetime.now()
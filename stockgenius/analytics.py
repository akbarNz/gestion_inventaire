from datetime import datetime
from stockgenius.inventory import Inventory
from stockgenius.abstract_order import OrderStatus

class SalesAnalytics:
    """Handles sales analytics and dashboard generation."""
    
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def generate_dashboard(self) -> str:
        """Generate sales analytics dashboard."""
        dashboard = []
        dashboard.append("=" * 80)
        dashboard.append("SALES ANALYTICS DASHBOARD")
        dashboard.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        dashboard.append("=" * 80)

        # Sales Overview
        total_sales = self._calculate_total_sales()
        completed_orders = len([o for o in self.inventory.sale_orders 
                              if o.status == OrderStatus.DELIVERED])
        dashboard.append("\nSALES OVERVIEW")
        dashboard.append("-" * 80)
        dashboard.append(f"Total Sales Revenue: ${total_sales:.2f}")
        dashboard.append(f"Completed Orders: {completed_orders}")
        dashboard.append(f"Average Order Value: ${total_sales/completed_orders:.2f}" if completed_orders else "Average Order Value: $0.00")

        # Top Products
        dashboard.append("\nTOP SELLING PRODUCTS")
        dashboard.append("-" * 80)
        top_products = self._get_top_products(5)
        for product, quantity in top_products:
            dashboard.append(f"{product.name}: {quantity} units")

        # Category Performance
        dashboard.append("\nCATEGORY PERFORMANCE")
        dashboard.append("-" * 80)
        category_sales = self._get_category_sales()
        for category, sales in category_sales:
            dashboard.append(f"{category}: ${sales:.2f}")

        # Stock Status
        dashboard.append("\nSTOCK STATUS")
        dashboard.append("-" * 80)
        low_stock = self._get_low_stock_products()
        for product in low_stock:
            dashboard.append(f"Low Stock Alert - {product.name}: {product.quantity} units remaining")

        return "\n".join(dashboard)

    def _calculate_total_sales(self) -> float:
        """Calculate total sales revenue from delivered orders."""
        return sum(order.total_price for order in self.inventory.sale_orders 
                  if order.status == OrderStatus.DELIVERED)

    def _get_top_products(self, limit: int = 5) -> list:
        """Get top selling products by quantity."""
        product_sales = {}
        for order in self.inventory.sale_orders:
            if order.status == OrderStatus.DELIVERED:
                for product in order.products:
                    if product.product_id in product_sales:
                        product_sales[product.product_id][1] += product.quantity
                    else:
                        product_sales[product.product_id] = [product, product.quantity]
        
        sorted_products = sorted(product_sales.values(), 
                               key=lambda x: x[1], 
                               reverse=True)
        return sorted_products[:limit]

    def _get_category_sales(self) -> list:
        """Get sales performance by category."""
        category_sales = {}
        for order in self.inventory.sale_orders:
            if order.status == OrderStatus.DELIVERED:
                for product in order.products:
                    category = product.category.name
                    if category in category_sales:
                        category_sales[category] += product.price * product.quantity
                    else:
                        category_sales[category] = product.price * product.quantity
        
        return sorted(category_sales.items(), 
                     key=lambda x: x[1], 
                     reverse=True)

    def _get_low_stock_products(self) -> list:
        """Get products with stock below reorder point."""
        return [product for product in self.inventory.products 
                if product.quantity <= product.reorder_point]
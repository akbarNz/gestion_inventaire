import unittest
from stockgenius.analytics import SalesAnalytics
from stockgenius.inventory import Inventory
from stockgenius.product import Product
from stockgenius.category import Category
from stockgenius.sale_order import SaleOrder
from stockgenius.abstract_order import OrderStatus

class TestSalesAnalytics(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.category = Category("Electronics", 0.2)
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category)
        self.inventory.add_category(self.category)
        self.inventory.add_product(self.product)
        
        # Create a test order
        self.order = SaleOrder("SO001", [self.product])
        self.order.status = OrderStatus.DELIVERED
        self.inventory.add_sale_order(self.order)
        
        self.analytics = SalesAnalytics(self.inventory)

    def test_calculate_total_sales(self):
        total = self.analytics._calculate_total_sales()
        self.assertEqual(total, self.product.calculate_price_with_vat())

    def test_get_top_products(self):
        top_products = self.analytics._get_top_products()
        self.assertEqual(len(top_products), 1)
        self.assertEqual(top_products[0][0], self.product)

    def test_get_category_sales(self):
        category_sales = self.analytics._get_category_sales()
        self.assertEqual(len(category_sales), 1)
        self.assertEqual(category_sales[0][0], "Electronics")

    def test_get_low_stock_products(self):
        self.product.quantity = self.product.reorder_point
        low_stock = self.analytics._get_low_stock_products()
        self.assertIn(self.product, low_stock)

if __name__ == '__main__':
    unittest.main()
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.sale_order import SaleOrder  # Changed from Order
from stockgenius.product import Product
from stockgenius.category import Category


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", 0.2)
        self.product1 = Product("P001", "Laptop", 10, 1500.0, self.category)
        self.product2 = Product("P002", "Smartphone", 20, 800.0, self.category)
        self.order = SaleOrder("O001", [self.product1])

    def test_calculate_total_price(self):
        self.assertEqual(self.order.calculate_total_price(), 1500.0)

    def test_add_product(self):
        self.order.add_product(self.product2)
        self.assertIn(self.product2, self.order.products)
        self.assertEqual(self.order.total_price, 2300.0)

    def test_remove_product(self):
        self.order.add_product(self.product2)
        self.order.remove_product(self.product1)
        self.assertNotIn(self.product1, self.order.products)
        self.assertEqual(self.order.total_price, 800.0)

    def test_search_product_by_id(self):
        self.order.add_product(self.product2)
        product = self.order.seach_product_by_id("P002")
        self.assertEqual(product, self.product2)

    def test_list_products(self):
        self.order.add_product(self.product2)
        product_list = self.order.list_products()
        self.assertIn("P001 | Laptop | 1500.0", product_list)
        self.assertIn("P002 | Smartphone | 800.0", product_list)

    def test_str(self):
        order_str = str(self.order)
        self.assertIn("Order ID: O001", order_str)
        self.assertIn("Total price: 1500.0", order_str)
        self.assertIn("Products: 1", order_str)

if __name__ == '__main__':
    unittest.main()
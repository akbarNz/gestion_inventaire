import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.order import Order
from stockgenius.product import Product
from stockgenius.supplier import Supplier


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.category = Category("Electronics", 0.2)
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category)
        self.order = Order("O001", [self.product])

    def test_add_product(self):
        self.inventory.add_product(self.product)
        self.assertIn(self.product, self.inventory.products)

    def test_remove_product(self):
        self.inventory.add_product(self.product)
        self.inventory.remove_product(self.product)
        self.assertNotIn(self.product, self.inventory.products)

    def test_get_product_by_id(self):
        self.inventory.add_product(self.product)
        product = self.inventory.get_product_by_id("P001")
        self.assertEqual(product, self.product)

    def test_get_products_by_category(self):
        self.inventory.add_product(self.product)
        products = self.inventory.get_products_by_category("Electronics")
        self.assertIn(self.product, products)

    def test_search_products_by_name(self):
        self.inventory.add_product(self.product)
        products = self.inventory.search_products_by_name("Laptop")
        self.assertIn(self.product, products)

    def test_search_products_by_price_range(self):
        self.inventory.add_product(self.product)
        products = self.inventory.search_products_by_price_range(1000, 2000)
        self.assertIn(self.product, products)

    def test_update_product_price(self):
        self.inventory.add_product(self.product)
        self.inventory.update_product_price("P001", 1600.0)
        self.assertEqual(self.product.price, 1600.0)

    def test_update_category_vat(self):
        self.inventory.add_category(self.category)
        self.inventory.update_category_vat("Electronics", 0.18)
        self.assertEqual(self.category.vat, 0.18)

    def test_calculate_product_price_with_vat(self):
        self.inventory.add_product(self.product)
        price_with_vat = self.inventory.calculate_product_price_with_vat("P001")
        self.assertEqual(price_with_vat, 1800.0)

    def test_generate_sales_summary(self):
        self.inventory.add_new_order(self.order)
        summary = self.inventory.generate_sales_summary()
        self.assertIn("Order ID: O001", summary)

    def test_add_new_order(self):
        self.inventory.add_new_order(self.order)
        self.assertIn(self.order, self.inventory.orders)

    def test_search_order(self):
        self.inventory.add_new_order(self.order)
        order = self.inventory.search_order("O001")
        self.assertEqual(order, self.order)

    def test_remove_order(self):
        self.inventory.add_new_order(self.order)
        self.inventory.remove_order("O001")
        self.assertNotIn(self.order, self.inventory.orders)

if __name__ == '__main__':
    unittest.main()
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category
from stockgenius.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", 0.2)
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category)

    def test_get_price(self):
        self.assertEqual(self.product.price, 1500.0)

    def test_set_price(self):
        self.product.price = 1600.0
        self.assertEqual(self.product.price, 1600.0)

    def test_get_name(self):
        self.assertEqual(self.product.name, "Laptop")

    def test_set_name(self):
        self.product.name = "Gaming Laptop"
        self.assertEqual(self.product.name, "Gaming Laptop")

    def test_set_quantity(self):
        self.product.quantity = 20
        self.assertEqual(self.product.quantity, 20)
        with self.assertRaises(TypeError):
            self.product.quantity = "twenty"

    def test_calculate_price_with_vat(self):
        self.assertEqual(self.product.calculate_price_with_vat(), 1800.0)

    def test_str(self):
        self.assertEqual(str(self.product), "Product(P001, Laptop, 10, 1500.0, Electronics)")

if __name__ == '__main__':
    unittest.main()
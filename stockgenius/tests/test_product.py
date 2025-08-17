import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category
from stockgenius.product import Product
from stockgenius.supplier import Supplier

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.category = Category("Electronics", 0.2)
        self.supplier = Supplier("S001", "TechWorld", "John Smith", "john@techworld.com", "123-456-7890", "123 Tech St")
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category, self.supplier)

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
        expected = "Product(P001, Laptop, 10, 1500.0, Electronics)"
        self.assertEqual(str(self.product), expected)

    # Add supplier-related tests
    def test_get_supplier(self):
        self.assertEqual(self.product.supplier, self.supplier)

    def test_set_supplier(self):
        new_supplier = Supplier("S002", "NewTech", "Jane Doe", "jane@newtech.com", "987-654-3210", "456 New St")
        self.product.supplier = new_supplier
        self.assertEqual(self.product.supplier, new_supplier)

if __name__ == '__main__':
    unittest.main()
import unittest
import os
import sys
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.managment.product_management import (
    product_management,
    choose_option,
    add_product,
    change_product,
    remove_product,
    search_products
)
from stockgenius.product import Product
from stockgenius.supplier import Supplier


class TestProductManagement(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.category = Category("Electronics", 0.2)
        self.supplier = Supplier("S001", "TechWorld", "John Smith", "john@techworld.com", "123-456-7890", "123 Tech St")
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category, self.supplier)
        self.inventory.add_product(self.product)
        self.inventory.add_category(self.category)
        self.inventory.add_supplier(self.supplier)

    @patch('builtins.input', side_effect=['q'])
    @patch('builtins.print')
    def test_product_management_quit(self, mock_print, mock_input):
        product_management(self.inventory)
        mock_print.assert_any_call('you quit successefuly')

    @patch('builtins.input', side_effect=['a', 'P002', 'Smartphone', '20', '800.0', 'Electronics', 'S001', 'q'])
    @patch('builtins.print')
    def test_add_product(self, mock_print, mock_input):
        product_management(self.inventory)
        product = self.inventory.get_product_by_id('P002')
        self.assertIsNotNone(product)
        self.assertEqual(product.supplier, self.supplier)

    @patch('builtins.input', side_effect=['r', 'P001', 'q'])
    @patch('builtins.print')
    def test_remove_product(self, mock_print, mock_input):
        product_management(self.inventory)
        self.assertIsNone(self.inventory.get_product_by_id('P001'))

    @patch('builtins.input', side_effect=[
        'u',             # update option
        'P001',          # product ID
        'Gaming Laptop', # new name
        '15',           # new quantity
        '1600.0',       # new price
        'Electronics',   # category name
        'S001',         # supplier ID
        '',             # empty input to keep current supplier
        'q'             # quit
    ])
    def test_change_product(self, mock_input):  # Remove self.mock_input parameter
        """Test product change through product management."""
        product_management(self.inventory)
        product = self.inventory.get_product_by_id('P001')
        self.assertEqual(product.name, 'Gaming Laptop')
        self.assertEqual(product.quantity, 15)
        self.assertEqual(product.price, 1600.0)
        self.assertEqual(product.supplier, self.supplier)

    @patch('builtins.input', side_effect=[
        'Gaming Laptop',  # new name
        '15',            # new quantity
        '1600.0',        # new price
        'Electronics',   # category name
        'S001',         # supplier ID
        ''              # empty input to keep current supplier
    ])
    def test_change_product_function(self, mock_input):
        """Test changing product attributes directly."""
        change_product(self.inventory, 'P001')
        product = self.inventory.get_product_by_id('P001')
        self.assertEqual(product.name, 'Gaming Laptop')
        self.assertEqual(product.quantity, 15)
        self.assertEqual(product.price, 1600.0)
        self.assertEqual(product.supplier, self.supplier)

    @patch('builtins.input', side_effect=['s', 'n', 'Laptop', 'q'])
    @patch('builtins.print')
    def test_search_products_by_name(self, mock_print, mock_input):
        product_management(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.input', side_effect=['s', 'i', 'P001', 'q'])
    @patch('builtins.print')
    def test_search_products_by_id(self, mock_print, mock_input):
        product_management(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.input', side_effect=['s', 'p', '1000', '2000', 'q'])
    @patch('builtins.print')
    def test_search_products_by_price_range(self, mock_print, mock_input):
        product_management(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.input', side_effect=['s', 'c', 'Electronics', 'q'])
    @patch('builtins.print')
    def test_search_products_by_category(self, mock_print, mock_input):
        product_management(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.input', side_effect=['a'])
    def test_choose_option_add(self, mock_input):
        option = choose_option()
        self.assertEqual(option, 'a')

    @patch('builtins.input', side_effect=['P002', 'Smartphone', '20', '800.0', 'Electronics', 'S001'])
    def test_add_product_function(self, mock_input):
        add_product(self.inventory)
        product = self.inventory.get_product_by_id('P002')
        self.assertIsNotNone(product)
        self.assertEqual(product.supplier, self.supplier)

    @patch('builtins.input', side_effect=['P001', 'Gaming Laptop', '15', '1600.0', 'Electronics', 'S002', 'y',
                                         'NewSupplier', 'Jane Doe', 'jane@supplier.com', '987-654-3210', '456 Supplier St'])
    def test_change_product_function(self, mock_input):
        change_product(self.inventory, 'P001')
        product = self.inventory.get_product_by_id('P001')
        self.assertEqual(product.name, 'Gaming Laptop')
        self.assertEqual(product.quantity, 15)
        self.assertEqual(product.price, 1600.0)

    @patch('builtins.input', side_effect=['P001'])
    def test_remove_product_function(self, mock_input):
        remove_product(self.inventory)
        self.assertIsNone(self.inventory.get_product_by_id('P001'))

    @patch('builtins.input', side_effect=['n', 'Laptop'])
    @patch('builtins.print')
    def test_search_products_function(self, mock_print, mock_input):
        search_products(self.inventory)
        mock_print.assert_any_call(self.product)

if __name__ == '__main__':
    unittest.main()
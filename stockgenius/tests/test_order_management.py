import unittest
import os
import sys
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.managment.order_management import (
    order_management,
    choose_option,
    create_order,
    add_products_to_order,
    change_order,
    remove_order,
    search_order,
    list_orders
)
from stockgenius.sale_order import Order
from stockgenius.product import Product


class TestOrderManagement(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.category = Category("Electronics", 0.2)
        self.product = Product("P001", "Laptop", 10, 1500.0, self.category)
        self.order = Order("O001", [self.product])
        self.inventory.add_product(self.product)
        self.inventory.add_category(self.category)
        self.inventory.add_new_order(self.order)

    @patch('builtins.input', side_effect=['q'])
    @patch('builtins.print')
    def test_order_management_quit(self, mock_print, mock_input):
        order_management(self.inventory)
        mock_print.assert_any_call('you quit successefuly')

    @patch('builtins.input', side_effect=['c', 'O002', 'P001', 'n', 'q'])
    @patch('builtins.print')
    def test_create_order(self, mock_print, mock_input):
        order_management(self.inventory)
        self.assertIsNotNone(self.inventory.get_order_by_id('O002'))

    @patch('builtins.input', side_effect=['r', 'O001', 'q'])
    @patch('builtins.print')
    def test_remove_order(self, mock_print, mock_input):
        order_management(self.inventory)
        self.assertIsNone(self.inventory.get_order_by_id('O001'))

    @patch('builtins.input', side_effect=['u', 'O001', 'a', 'P001', 'n', 'q'])
    @patch('builtins.print')
    def test_change_order_add_product(self, mock_print, mock_input):
        order_management(self.inventory)
        order = self.inventory.get_order_by_id('O001')
        self.assertEqual(len(order.products), 2)

    @patch('builtins.input', side_effect=['u', 'O001', 'r', 'P001', 'n', 'q'])
    @patch('builtins.print')
    def test_change_order_remove_product(self, mock_print, mock_input):
        order_management(self.inventory)
        order = self.inventory.get_order_by_id('O001')
        self.assertEqual(len(order.products), 0)

    @patch('builtins.input', side_effect=['s', 'O001', 'l', 'q'])
    @patch('builtins.print')
    def test_search_order_list(self, mock_print, mock_input):
        order_management(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.input', side_effect=['s', 'O001', 'c', 'a', 'P001', 'n', 'q'])
    @patch('builtins.print')
    def test_search_order_change(self, mock_print, mock_input):
        order_management(self.inventory)
        order = self.inventory.get_order_by_id('O001')
        self.assertEqual(len(order.products), 2)

    @patch('builtins.input', side_effect=['l', 'q'])
    @patch('builtins.print')
    def test_list_orders(self, mock_print, mock_input):
        order_management(self.inventory)
        mock_print.assert_any_call('Orders in the inventory:\n')

    @patch('builtins.input', side_effect=['c'])
    def test_choose_option_create(self, mock_input):
        option = choose_option()
        self.assertEqual(option, 'c')

    @patch('builtins.input', side_effect=['O002', 'P001', 'n'])
    def test_create_order_function(self, mock_input):
        create_order(self.inventory)
        self.assertIsNotNone(self.inventory.get_order_by_id('O002'))

    @patch('builtins.input', side_effect=['P001', 'n'])
    def test_add_products_to_order_function(self, mock_input):
        products = add_products_to_order(self.inventory)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].product_id, 'P001')

    @patch('builtins.input', side_effect=['a', 'P001', 'n', 'q'])
    def test_change_order_function_add(self, mock_input):
        change_order(self.inventory, 'O001')
        order = self.inventory.get_order_by_id('O001')
        self.assertEqual(len(order.products), 2)

    @patch('builtins.input', side_effect=['r', 'P001', 'n', 'q'])
    def test_change_order_function_remove(self, mock_input):
        change_order(self.inventory, 'O001')
        order = self.inventory.get_order_by_id('O001')
        self.assertEqual(len(order.products), 0)

    @patch('builtins.input', side_effect=['O001'])
    def test_remove_order_function(self, mock_input):
        remove_order(self.inventory)
        self.assertIsNone(self.inventory.get_order_by_id('O001'))

    @patch('builtins.input', side_effect=['O001', 'l'])
    @patch('builtins.print')
    def test_search_order_function(self, mock_print, mock_input):
        search_order(self.inventory)
        mock_print.assert_any_call(self.product)

    @patch('builtins.print')
    def test_list_orders_function(self, mock_print):
        list_orders(self.inventory)
        mock_print.assert_any_call('Orders in the inventory:\n')

if __name__ == '__main__':
    unittest.main()
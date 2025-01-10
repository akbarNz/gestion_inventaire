import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.managment.category_management import (
    category_management,
    choose_option,
    create_category,
    remove_category,
    change_vat,
    list_categories
)


class TestCategoryManagement(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.category = Category("Electronics", 0.2)
        self.inventory.add_category(self.category)

    @patch('builtins.input', side_effect=['q'])
    @patch('builtins.print')
    def test_category_management_quit(self, mock_print, mock_input):
        category_management(self.inventory)
        mock_print.assert_any_call('You quit successfully')

    @patch('builtins.input', side_effect=['c', 'NewCategory', '0.15', 'q'])
    @patch('builtins.print')
    def test_create_category(self, mock_print, mock_input):
        category_management(self.inventory)
        self.assertIsNotNone(self.inventory.search_category_by_name('NewCategory'))

    @patch('builtins.input', side_effect=['r', 'Electronics', 'q'])
    @patch('builtins.print')
    def test_remove_category(self, mock_print, mock_input):
        category_management(self.inventory)
        self.assertIsNone(self.inventory.search_category_by_name('Electronics'))

    @patch('builtins.input', side_effect=['v', 'Electronics', '0.18', 'q'])
    @patch('builtins.print')
    def test_change_vat(self, mock_print, mock_input):
        category_management(self.inventory)
        self.assertEqual(self.category.vat, 0.18)

    @patch('builtins.input', side_effect=['l', 'q'])
    @patch('builtins.print')
    def test_list_categories(self, mock_print, mock_input):
        category_management(self.inventory)
        mock_print.assert_any_call('Categories in the inventory:\n')

    @patch('builtins.input', side_effect=['c'])
    def test_choose_option_create(self, mock_input):
        option = choose_option()
        self.assertEqual(option, 'c')

    @patch('builtins.input', side_effect=['NewCategory', '0.15'])
    def test_create_category_function(self, mock_input):
        create_category(self.inventory)
        self.assertIsNotNone(self.inventory.search_category_by_name('NewCategory'))

    @patch('builtins.input', side_effect=['Electronics'])
    def test_remove_category_function(self, mock_input):
        remove_category(self.inventory)
        self.assertIsNone(self.inventory.search_category_by_name('Electronics'))

    @patch('builtins.input', side_effect=['Electronics', '0.18'])
    def test_change_vat_function(self, mock_input):
        change_vat(self.inventory)
        self.assertEqual(self.category.vat, 0.18)

    @patch('builtins.print')
    def test_list_categories_function(self, mock_print):
        list_categories(self.inventory)
        mock_print.assert_any_call('Categories in the inventory:\n')

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from io import StringIO
from stockgenius.managment.supplier_management import (
    supplier_management,
    choose_option,
    create_supplier,
    remove_supplier,
    update_supplier,
    search_supplier
)
from stockgenius.inventory import Inventory
from stockgenius.supplier import Supplier

class TestSupplierManagement(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.supplier = Supplier(
            "S001", 
            "Tech Supplies Inc", 
            "John Doe", 
            "john@techsupplies.com", 
            "123-456-7890", 
            "123 Tech Street"
        )
        self.inventory.add_supplier(self.supplier)

    @patch('builtins.input', side_effect=['q'])
    @patch('builtins.print')
    def test_supplier_management_quit(self, mock_print, mock_input):
        supplier_management(self.inventory)
        mock_print.assert_any_call('you quit successfully')

    @patch('builtins.input', side_effect=['S002', 'New Supplier', 'Jane Doe', 'jane@supplier.com', '987-654-3210', '456 Supplier St'])
    def test_create_supplier(self, mock_input):
        create_supplier(self.inventory)
        supplier = self.inventory.get_supplier_by_id('S002')
        self.assertIsNotNone(supplier)
        self.assertEqual(supplier.name, 'New Supplier')

    @patch('builtins.input', return_value='S001')
    def test_remove_supplier(self, mock_input):
        remove_supplier(self.inventory)
        self.assertIsNone(self.inventory.get_supplier_by_id('S001'))

    @patch('builtins.input', side_effect=['S001', 'newemail@supplier.com', '987-654-3210', 'Jane Doe'])
    def test_update_supplier(self, mock_input):
        update_supplier(self.inventory)
        supplier = self.inventory.get_supplier_by_id('S001')
        self.assertEqual(supplier.email, 'newemail@supplier.com')
        self.assertEqual(supplier.phone, '987-654-3210')
        self.assertEqual(supplier.contact_person, 'Jane Doe')

    @patch('builtins.input', return_value='S001')
    @patch('builtins.print')
    def test_search_supplier(self, mock_print, mock_input):
        search_supplier(self.inventory)
        mock_print.assert_any_call(self.supplier)

    @patch('builtins.input', return_value='c')
    def test_choose_option(self, mock_input):
        option = choose_option()
        self.assertEqual(option, 'c')

if __name__ == '__main__':
    unittest.main()
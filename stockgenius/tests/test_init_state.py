import csv
import os
import sys
import shutil
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.init_state import init_state
from stockgenius.inventory import Inventory


class TestInitState(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create sample CSV files
        self.create_csv_file('electronics.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat'],
            ['P001', 'Laptop', '10', '1500.0', 'Electronics', '0.2'],
            ['P002', 'Smartphone', '20', '800.0', 'Electronics', '0.2']
        ])
        
        self.create_csv_file('furniture.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat'],
            ['P003', 'Chair', '30', '50.0', 'Furniture', '0.1'],
            ['P004', 'Table', '10', '150.0', 'Furniture', '0.1']
        ])
        
        self.create_csv_file('clothing.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat'],
            ['P005', 'T-Shirt', '50', '20.0', 'Clothing', '0.15'],
            ['P006', 'Jeans', '40', '40.0', 'Clothing', '0.15']
        ])

    def create_csv_file(self, filename, rows):
        with open(os.path.join(self.test_dir, filename), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_init_state(self):
        inventory = init_state(self.test_dir)
        
        # Check if inventory is an instance of Inventory
        self.assertIsInstance(inventory, Inventory)
        
        # Check if categories are correctly added
        self.assertEqual(len(inventory.categories), 3)
        self.assertIsNotNone(inventory.search_category_by_name('Electronics'))
        self.assertIsNotNone(inventory.search_category_by_name('Furniture'))
        self.assertIsNotNone(inventory.search_category_by_name('Clothing'))
        
        # Check if products are correctly added
        self.assertEqual(len(inventory.products), 6)
        self.assertIsNotNone(inventory.get_product_by_id('P001'))
        self.assertIsNotNone(inventory.get_product_by_id('P002'))
        self.assertIsNotNone(inventory.get_product_by_id('P003'))
        self.assertIsNotNone(inventory.get_product_by_id('P004'))
        self.assertIsNotNone(inventory.get_product_by_id('P005'))
        self.assertIsNotNone(inventory.get_product_by_id('P006'))

if __name__ == '__main__':
    unittest.main()
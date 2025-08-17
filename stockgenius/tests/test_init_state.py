import csv
import os
import sys
import shutil
import unittest

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from stockgenius.inventory import Inventory
from stockgenius.init_state import init_state
from stockgenius.category import Category
from stockgenius.product import Product
from stockgenius.supplier import Supplier


class TestInitState(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create suppliers CSV file
        self.create_csv_file('suppliers.csv', [
            ['supplier_id', 'name', 'contact_person', 'email', 'phone', 'address'],
            ['S001', 'TechWorld Inc', 'John Smith', 'john@techworld.com', '123-456-7890', '123 Tech Street NY'],
            ['S002', 'FurniturePro', 'Alice Johnson', 'alice@furniturepro.com', '234-567-8901', '456 Wood Avenue CA'],
            ['S003', 'FashionStyle', 'Bob Wilson', 'bob@fashionstyle.com', '345-678-9012', '789 Fashion Boulevard FL']
        ])
        
        # Create sample product CSV files with supplier_id
        self.create_csv_file('electronics.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat', 'supplier_id'],
            ['P001', 'Laptop', '10', '1500.0', 'Electronics', '0.2', 'S001'],
            ['P002', 'Smartphone', '20', '800.0', 'Electronics', '0.2', 'S001']
        ])
        
        self.create_csv_file('furniture.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat', 'supplier_id'],
            ['P003', 'Chair', '30', '50.0', 'Furniture', '0.1', 'S002'],
            ['P004', 'Table', '10', '150.0', 'Furniture', '0.1', 'S002']
        ])
        
        self.create_csv_file('clothing.csv', [
            ['product_id', 'name', 'quantity', 'price', 'category_name', 'vat', 'supplier_id'],
            ['P005', 'T-Shirt', '50', '20.0', 'Clothing', '0.15', 'S003'],
            ['P006', 'Jeans', '40', '40.0', 'Clothing', '0.15', 'S003']
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
        
        # Check if suppliers are correctly added
        self.assertEqual(len(inventory.suppliers), 3)
        self.assertIsNotNone(inventory.get_supplier_by_id('S001'))
        self.assertIsNotNone(inventory.get_supplier_by_id('S002'))
        self.assertIsNotNone(inventory.get_supplier_by_id('S003'))
        
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

        # Check if products are correctly associated with suppliers
        supplier1 = inventory.get_supplier_by_id('S001')
        supplier2 = inventory.get_supplier_by_id('S002')
        supplier3 = inventory.get_supplier_by_id('S003')
        
        self.assertEqual(len(supplier1.products), 2)  # Electronics products
        self.assertEqual(len(supplier2.products), 2)  # Furniture products
        self.assertEqual(len(supplier3.products), 2)  # Clothing products
        
        # Check specific product-supplier associations
        product1 = inventory.get_product_by_id('P001')
        self.assertEqual(product1.supplier, supplier1)
        
        product3 = inventory.get_product_by_id('P003')
        self.assertEqual(product3.supplier, supplier2)
        
        product5 = inventory.get_product_by_id('P005')
        self.assertEqual(product5.supplier, supplier3)

if __name__ == '__main__':
    unittest.main()
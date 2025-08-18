import csv
import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.product import Product
from stockgenius.sale_order import SaleOrder  # Changed from Order
from stockgenius.supplier import Supplier


def init_state(data_dir):
    """Process the files and create the initial state of the app.
    
    Args:
        data_dir (str): The pathname of the data files directory to process.
    
    Returns: 
        the inventory (Inventory) object.
    """
    inventory = Inventory()
    
    # First, load suppliers
    suppliers = {}
    with open(os.path.join(data_dir, 'suppliers.csv'), newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            supplier = Supplier(
                row['supplier_id'],
                row['name'],
                row['contact_person'],
                row['email'],
                row['phone'],
                row['address']
            )
            suppliers[row['supplier_id']] = supplier
            inventory.add_supplier(supplier)

    # Then load products
    product_files = [f for f in os.listdir(data_dir) if f.endswith('.csv') and f != 'suppliers.csv']
    
    for file in product_files:
        with open(os.path.join(data_dir, file), newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                cat = Category(row['category_name'], float(row['vat']))
                supplier = suppliers.get(row['supplier_id'])
                product = Product(
                    row['product_id'],
                    row['name'],
                    int(row['quantity']),
                    float(row['price']),
                    cat,
                    supplier
                )

                # add a category if not existent 
                if inventory.search_category_by_name(cat.name) is None:
                    inventory.add_category(cat)
                # add a product to the inventory
                inventory.add_product(product)
                # add product to supplier's catalog
                if supplier:
                    supplier.add_product(product)
    
    return inventory



import csv
import os
from product import Product
from category import Category
from inventory import Inventory

def init_state(data_dir):
    """Process the files and create the initial state of the app.
    
    Args:
        data_dir (str): The pathname of the data files directory to process.
    
    Returns: 
        the invetory (Inventory) object.
    """
    inventory = Inventory()
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    for file in all_files:
        with open(file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                cat = Category(row['category_name'], row['vat'])
                product = Product(row['product_id'], row['name'], row['quantity'], row['price'], cat)

                # add a category if not exitent 
                if inventory.search_category_by_name(cat.name) is None:
                    inventory.add_category(cat)
                # add a product to the inventory
                inventory.add_product(product)
    
    return inventory



import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from stockgenius.category import Category
from stockgenius.inventory import Inventory
from stockgenius.product import Product
from stockgenius.supplier import Supplier
from stockgenius.managment.supplier_management import create_supplier


def product_management(inventory:Inventory):
    """Manage products in the inventory.
    
    Args:
        inventory (Inventory): the inventory
    """
    print(inventory.list_products())
    done = False
    while not done:
        message = f"{'-'*106}\nTo add a product enter [a]\n to remove a product enter [r]\n to update a product enter [u]\nto search products enter [s]\n to list enter [l]\n to quit product management enter [q]\n{'-'*106}"
        print(message)
        opt = choose_option()

        if opt == 'a':
            print("Add a product")
            add_product(inventory)
        elif opt == 'r':
            print('Remove a product')
            remove_product(inventory)
        elif opt == 'u':
            print('Update a product')
            product_id = input("Enter the product ID to update: ")
            if inventory.get_product_by_id(product_id) is None:
                print("Product not found")
            else:
                change_product(inventory, product_id)
        elif opt == 's':
            print('Search products')
            search_products(inventory)
        elif opt == 'l':
            print(inventory.list_products())
        elif opt == 'q':
            done = True
            print('you quit successefuly')

def choose_option():
    """Choose an option to manage.
    
    Returns: opt (str) the choosen option
    """
    opt = input("enter an option [a/r/u/s/l/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'aruslq':
            valid = True
        else:
            print("option not valid")
            opt = input("enter an option [a/r/u/s/l/q]: ")
    
    return opt

def add_product(inventory:Inventory):
    """Input product data.
    
    Args:
        inventory (Inventory): the inventory
    """
    product_id = input("Enter the product ID eg P003 : ")
    is_correct = False
    change_existing_product = 'n'
    while not is_correct:
        if inventory.get_product_by_id(product_id) is not None:
            print("Product ID already exists")
            change_existing_product = input("Do you want to change the existing product? [y/n]: ")
            if change_existing_product == 'y':
                is_correct = True
            else:
                product_id = input("Enter the product ID eg P003 : ")
        else: 
            is_correct = True

    if change_existing_product == 'y':
        # change the existing product
        change_product(inventory, product_id)
    else:
        # add a new product
        name = input("Enter the product name: ")

        quantity = input("Enter the product quantity: ")
        is_gt_zero = False
        while not is_gt_zero:
            if int(quantity) < 0:
                print("Quantity must be greater or equal zero")
                quantity = input("Enter the product quantity: ")
            else:
                is_gt_zero = True
        
        price = input("Enter the product price: ")
        is_gt_zero = False
        while not is_gt_zero:
            if float(price) <= 0:
                print("Price must be greater or than zero")
                price = input("Enter the product price: ")
            else:
                is_gt_zero = True
        
        category_name = input("Enter the category name: ")
        category = None
        if inventory.search_category_by_name(category_name) is None:
            print("Category does not exist")
            vat =float(input("Enter the category VAT: "))
            is_gt_zero = False
            while not is_gt_zero:
                if float(vat) < 0:
                    print("VAT must be greater than zero")
                    vat = float(input("Enter the category VAT: "))
                else:
                    is_gt_zero = True
        
            if is_gt_zero:
                # add the category to the inventory
                category = Category(category_name, vat)
                inventory.add_category(category)

        # Add supplier handling
        supplier_id = input("Enter the supplier ID (eg. S001): ")
        supplier = None
        if inventory.get_supplier_by_id(supplier_id) is None:
            print("Supplier does not exist")
            create_new = input("Do you want to create a new supplier? [y/n]: ")
            if create_new.lower() == 'y':
                supplier = create_supplier(inventory)
            else:
                supplier_id = input("Enter an existing supplier ID: ")
                supplier = inventory.get_supplier_by_id(supplier_id)
                while supplier is None:
                    print("Supplier not found")
                    supplier_id = input("Enter an existing supplier ID: ")
                    supplier = inventory.get_supplier_by_id(supplier_id)
        else:
            supplier = inventory.get_supplier_by_id(supplier_id)

        # add the product to the inventory
        if category is None:
            category = inventory.search_category_by_name(category_name)

        product = Product(product_id, name, int(quantity), float(price), category, supplier)
        inventory.add_product(product)
        if supplier:
            supplier.add_product(product)

def change_product(inventory:Inventory, product_id:str):
    """Change an existing product.
    
    Args:
        inventory (Inventory): the inventory
        product_id (str): the product ID
    """
    product = inventory.get_product_by_id(product_id)
    print(f"Product ID: {product_id}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}, Category: {product.category.name}")
    
    name = input("Enter new name or Enter to keep current name: ")
    if name != '':
        product.name = name

    quantity = input("Enter new quantity or Enter to keep current quantity: ")
    if quantity != '':
        if int(quantity) < 0:
            print("Quantity must be positive")
        else:
            product.quantity = int(quantity)

    price = input("Enter the new product price or Enter to keep the current price: ")
    if price != '':
        is_gt_zero = False
        while not is_gt_zero:
            if float(price) <= 0:
                print("Price must be greater or than zero")
                price = input("Enter the new product price: ")
            else:
                is_gt_zero = True
        product.price = float(price)

    category_name = input("Enter the new category name or Enter to keep the current category: ")
    if category_name != '':
        if inventory.search_category_by_name(category_name) is None:
            print("Category does not exist")
            vat = float(input("Enter the category VAT: "))
            is_gt_zero = False
            while not is_gt_zero:
                if float(vat) < 0:
                    print("VAT must be greater than zero")
                    vat = float(input("Enter the category VAT: "))
                else:
                    is_gt_zero = True
            if is_gt_zero:
                # add the category to the inventory
                category = Category(category_name, vat)
                inventory.add_category(category)            
        product.category = inventory.search_category_by_name(category_name)

    # Add supplier changes
    supplier_id = input("Enter the new supplier ID or Enter to keep the current supplier: ")
    if supplier_id != '':
        supplier = inventory.get_supplier_by_id(supplier_id)
        if supplier is None:
            print("Supplier does not exist")
            create_new = input("Do you want to create a new supplier? [y/n]: ")
            if create_new.lower() == 'y':
                supplier = create_supplier(inventory)
            else:
                supplier_id = input("Enter an existing supplier ID: ")
                supplier = inventory.get_supplier_by_id(supplier_id)
                while supplier is None:
                    print("Supplier not found")
                    supplier_id = input("Enter an existing supplier ID: ")
                    supplier = inventory.get_supplier_by_id(supplier_id)
        
        # Remove product from old supplier's catalog
        if product.supplier:
            product.supplier.remove_product(product_id)
        
        # Update product's supplier and add to new supplier's catalog
        product.supplier = supplier
        supplier.add_product(product)

def remove_product(inventory:Inventory):
    """Remove a product from the inventory.
    
    Args:
        inventory (Inventory): the inventory
    """
    product_id = input("Enter the product ID to remove: ")
    product = inventory.get_product_by_id(product_id)
    if product is not None:
        inventory.remove_product(product)
    else:
        print("Product not found")

def search_products(inventory:Inventory):
    """Search products in the inventory.
    
    Args:
        inventory (Inventory): the inventory
    """
    print("Search products")
    opt = input("Search product by name [n]\nSearch product by product ID [i]\nSearch products by price range [p]\nSearch products by category name [c]\n enter [q] to quit")
    is_correct = False
    while not is_correct:
        if len(opt) == 1 and opt.lower() in 'nipcq':
            is_correct = True
        else:
            print("option not valid")
            opt = input("Search product by name [n]\nSearch product by product ID [i]\nSearch products by price range [p]\nSearch products by category name [c]\n enter [q] to quit")
    if opt == 'n':
        print("Search product by name")
        name = input("Enter the product name: ")
        products = inventory.search_products_by_name(name)
        if len(products) == 0:
            print("No products found")
        else:
            for product in products:
                print(product)
    elif opt == 'i':
        print("Search product by product ID")
        product_id = input("Enter the product ID: ")
        product = inventory.get_product_by_id(product_id)
        if product is None:
            print("Product not found")
        else:
            print(product)
    elif opt == 'p':
        print("Search products by price range")
        min_price = float(input("Enter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        products = inventory.search_products_by_price_range(min_price, max_price)
        if len(products) == 0:
            print("No products found")
        else:
            for product in products:
                print(product)
    elif opt == 'c':
        print("Search products by category name")
        category_name = input("Enter the category name: ")
        products = inventory.search_products_by_category_name(category_name)
        if len(products) == 0:
            print("No products found")
        else:
            for product in products:
                print(product)
    else:
        pass
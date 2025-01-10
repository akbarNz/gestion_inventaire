import sys
import os
from copy import deepcopy

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from stockgenius.inventory import Inventory
from stockgenius.order import Order


def order_management(inventory:Inventory):
    """Manage orders in the inventory. create, remove, search, and list orders.
    
    Args:
        inventory (Inventory): the inventory
    """
    # Print all orders
    list_orders(inventory)

    done = False
    while not done:
        message = f"{'-'*106}\nTo create an order enter [c], to change an order enter [u], to remove an order enter [r], to search an order enter [s], to list all orders enter [l], to quit order management enter [q]\n{'-'*106}"
        print(message)
        opt = choose_option()

        if opt == 'c':
            print("Create an order")
            create_order(inventory)
        elif opt == 'u':
            print('Change an order')
            order_id = input("Enter the order ID to update: ")
            if inventory.get_order_by_id(order_id) is None:
                print("Order not found")
            else:
                change_order(inventory, order_id)
        elif opt == 'r':
            print('Remove an order')
            remove_order(inventory)
        elif opt == 's':
            print('Search an order')
            search_order(inventory)
        elif opt == 'l':
            print('List all orders')
            list_orders(inventory)
        elif opt == 'q':
            done = True
            print('you quit successefuly')

def choose_option():
    """Choose an option to manage.
    
    Returns: opt (str) the choosen option
    """
    opt = input("enter an option [c/u/r/s/l/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'curslq':
            valid = True
        else:
            print("option not valid")
            opt = input("enter an option [c/u/r/s/l/q]: ")
    
    return opt

def create_order(inventory:Inventory):
    """Create an order.
    
    Args:
        inventory (Inventory): the inventory
    """
    order_id = input("Enter the order ID eg O003 : ")
    is_correct = False
    change_existing_order = 'n'
    while not is_correct:
        if inventory.get_order_by_id(order_id) is not None:
            print("Order ID already exists")
            change_existing_order = input("Do you want to change the existing order? [y/n]: ")
            if change_existing_order == 'y':
                is_correct = True
            else:
                order_id = input("Enter the order ID eg O003 : ")
        else: 
            # create the order and add it to the inventory orders eg Order('O001', products=[])
            products = add_products_to_order(inventory)
            order = Order(order_id, products)
            inventory.add_new_order(order)
            is_correct = True

    if change_existing_order == 'y':
        change_order(inventory, order_id)


def add_products_to_order(inventory:Inventory):
    """Add products to an order.
    
    Args:
        inventory (Inventory): the inventory
    
    Returns:
        products (list): the products to add to the order
    """
    products = []
    done = False
    # print all products
    print(inventory.list_products())
    while not done:
        product_id = input("Enter the product ID eg P003 : ")
        product = inventory.get_product_by_id(product_id)
        if product is not None:
            products.append(deepcopy(product))
            add_more_products = input("Do you want to add more products? [y/n]: ")
            if add_more_products == 'n':
                done = True
        else:
            print("Product not found")
    return products

def change_order(inventory:Inventory, order_id:str):
    """Change an order.
    
    Args:
        inventory (Inventory): the inventory
        order_id (str): the order ID
    """
    opt = input("Do you want to add or remove products to/from the order? Enter q to quit [a/r/q]: ")
    is_correct = False
    while not is_correct:
        if len(opt) == 1 and opt.lower() in 'arq':
            is_correct = True
        else:
            print("option not valid")
            opt = input("Do you want to add or remove products to/from the order? Enter q to quit [a/r/q]: ")
    
    if opt == 'a':
        # add products to the order
        order = inventory.get_order_by_id(order_id)
        products = add_products_to_order(inventory)
        order.products.extend(products)
        order.total_price = order.calculate_total_price()
    elif opt == 'r':
        # remove products from the order
        order = inventory.get_order_by_id(order_id)
        is_done = False
        while not is_done:
            product_id = input("Enter the product ID eg P003 : ")
            product = order.seach_product_by_id(product_id)
            if product is None:
                print("Product not found")
            else:
                order.remove_product(product)
                order.total_price = order.calculate_total_price()
            remove_more_products = input("Do you want to remove more products? [y/n]: ")
            if remove_more_products == 'n':
                is_done = True
    elif opt == 'q':
        # quit
        pass

def remove_order(inventory:Inventory):
    """Remove an order.
    
    Args:
        inventory (Inventory): the inventory
    """
    order_id = input("Enter the order ID eg O003 : ")
    order = inventory.get_order_by_id(order_id)
    if order is not None:
        inventory.remove_order(order_id)
    else:
        print("Order not found")

def search_order(inventory:Inventory):
    """Search an order.
    
    Args:
        inventory (Inventory): the inventory
    """
    order_id = input("Enter the order ID eg O003 : ")
    order = inventory.get_order_by_id(order_id)
    if order is not None:
        opt = input("Do you want to list or change the order? Enter q to quit [l/c/q]: ")
        is_correct = False
        while not is_correct:
            if len(opt) == 1 and opt.lower() in 'lcq':
                is_correct = True
            else:
                print("option not valid")
                opt = input("Do you want to list or change the order? Enter q to quit [l/c/q]: ")
        if opt == 'l':
            # list products in the order
            print(order.list_products())
        elif opt == 'c':
            change_order(inventory, order_id)
        elif opt == 'q':
            # quit
            pass
    else:
        print("Order not found")

def list_orders(inventory:Inventory):
    """List all orders.
    
    Args:
        inventory (Inventory): the inventory
    """
    res = "Orders in the inventory:\n"
    res = "-"*80 + '\n' + res + "-"*80 + "\n"
    for order in inventory.orders:
        res += str(order)
    print(res)
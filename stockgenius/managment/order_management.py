import sys
import os
from datetime import datetime

from stockgenius.inventory import Inventory
from stockgenius.sale_order import SaleOrder
from stockgenius.purchase_order import PurchaseOrder
from stockgenius.order_manager import OrderManager
from stockgenius.abstract_order import OrderStatus
from stockgenius.product import Product  # Add this import

def order_management(inventory: Inventory):
    """Manage orders in the inventory."""
    print("\nOrder Management")
    print(f"Sale Orders: {len(inventory.sale_orders)}")
    print(f"Purchase Orders: {len(inventory.purchase_orders)}")
    
    done = False
    order_manager = OrderManager(inventory)
    
    while not done:
        option = choose_option()
        if option == 'c':
            create_sale_order(inventory)
        elif option == 'v':
            view_orders(inventory)
        elif option == 'u':
            update_order_status(inventory)
        elif option == 'p':
            view_purchase_orders(inventory)
        elif option == 'a':
            order_manager.check_stock_levels()
            print("Automated purchase orders check completed")
        elif option == 'q':
            print('you quit successfully')
            done = True

def choose_option():
    """Choose an option for order management."""
    print("\nOrder Management Options:")
    print("c: Create new sale order")
    print("v: View all orders")
    print("u: Update order status")
    print("p: View purchase orders")
    print("a: Run automated purchase check")
    print("q: Quit")
    
    opt = input("enter an option [c/v/u/p/a/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'cvupaq':
            valid = True
        else:
            print("option not valid")
            opt = input("enter an option [c/v/u/p/a/q]: ")
    
    return opt

def create_sale_order(inventory: Inventory):
    """Create a new sale order with category-based product selection."""
    order_id = f"SO{datetime.now().strftime('%Y%m%d%H%M%S')}"
    products = []
    
    while True:
        # Display categories
        print("\nAvailable Categories:")
        print("-" * 50)
        for category in inventory.categories:
            print(f"- {category.name}")
        print("-" * 50)
        print("Enter 'back' to return to previous menu")
        print("Enter 'done' to finalize order")
        
        category_name = input("\nSelect a category: ")
        
        if category_name.lower() == 'done':
            break
        elif category_name.lower() == 'back':
            if len(products) > 0:
                if not confirm_order():
                    return
            break
            
        # Display products in selected category
        category_products = [p for p in inventory.products if p.category.name == category_name]
        if category_products:
            while True:
                print(f"\nProducts in {category_name}:")
                print("-" * 80)
                print(f"{'ID':<10} | {'Name':<20} | {'Quantity':<10} | {'Price':<10}")
                print("-" * 80)
                for product in category_products:
                    print(f"{product.product_id:<10} | {product.name:<20} | {product.quantity:<10} | {product.price:<10.2f}")
                print("-" * 80)
                print("Enter 'back' to return to categories")
                
                product_id = input("\nEnter product ID: ")
                if product_id.lower() == 'back':
                    break
                    
                selected_product = inventory.get_product_by_id(product_id)
                if selected_product and selected_product in category_products:
                    try:
                        quantity = int(input(f"Enter quantity (available: {selected_product.quantity}): "))
                        if 0 < quantity <= selected_product.quantity:
                            # Create a copy of the product with the requested quantity
                            order_product = Product(
                                selected_product.product_id,
                                selected_product.name,
                                quantity,
                                selected_product.price,
                                selected_product.category,
                                selected_product.supplier
                            )
                            products.append(order_product)
                            print(f"\nAdded {quantity} x {selected_product.name} to order")
                        else:
                            print("\nInvalid quantity!")
                    except ValueError:
                        print("\nInvalid quantity format!")
                else:
                    print("\nProduct not found!")
        else:
            print(f"\nNo products found in category {category_name}")
    
    if products and confirm_order():
        order = SaleOrder(order_id, products)
        inventory.add_sale_order(order)
        print(f"\nSale order {order_id} created successfully")
        print(f"Total price: {order.total_price:.2f}")

def confirm_order():
    """Ask for order confirmation."""
    while True:
        confirm = input("\nDo you want to confirm this order? (YES/NO): ").upper()
        if confirm == 'YES':
            return True
        elif confirm == 'NO':
            print("\nOrder cancelled")
            return False
        else:
            print("\nPlease enter YES or NO")

def view_orders(inventory: Inventory):
    """View all orders."""
    print("\nSale Orders:")
    for order in inventory.sale_orders:
        print(order)
        print(order.list_products())
    
    print("\nPurchase Orders:")
    for order in inventory.purchase_orders:
        print(order)
        print(f"Supplier: {order.supplier.name}")
        print(order.list_products())

def update_order_status(inventory: Inventory):
    """Update order status and handle quantity updates."""
    order_id = input("Enter order ID: ")
    new_status = input("Enter new status (pending/confirmed/shipped/delivered/cancelled): ")
    
    try:
        status = OrderStatus(new_status)
        orders_updated = False
        
        # Update all orders with the same ID
        for order in inventory.purchase_orders:
            if order.order_id == order_id:
                old_status = order.status
                order.status = status
                orders_updated = True
                
                # Update product quantities if status changed to delivered
                if status == OrderStatus.DELIVERED and old_status != OrderStatus.DELIVERED:
                    for product in order.products:
                        original_product = inventory.get_product_by_id(product.product_id)
                        if original_product:
                            original_product.quantity += product.quantity
                    print(f"Updated quantities for order {order_id}")

        for order in inventory.sale_orders:
            if order.order_id == order_id:
                old_status = order.status
                order.status = status
                orders_updated = True
                
                # Decrease product quantities if status changed to delivered
                if status == OrderStatus.DELIVERED and old_status != OrderStatus.DELIVERED:
                    for product in order.products:
                        original_product = inventory.get_product_by_id(product.product_id)
                        if original_product:
                            original_product.quantity -= product.quantity
                    print(f"Updated quantities for order {order_id}")
        
        if orders_updated:
            print(f"Updated order {order_id} status to {new_status}")
        else:
            print(f"Order {order_id} not found")
            
    except ValueError:
        print("Invalid status")

def view_purchase_orders(inventory: Inventory):
    """View purchase orders."""
    print("\nPurchase Orders:")
    for order in inventory.purchase_orders:
        print(order)
        print(f"Supplier: {order.supplier.name}")
        print(f"Expected Delivery: {order.expected_delivery.strftime('%Y-%m-%d')}")
        print(order.list_products())
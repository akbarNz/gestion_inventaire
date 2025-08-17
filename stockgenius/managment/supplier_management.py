import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stockgenius.supplier import Supplier
from stockgenius.inventory import Inventory

def supplier_management(inventory: Inventory):
    """Manage suppliers in the inventory."""
    print(inventory.list_suppliers())
    
    done = False
    while not done:
        option = choose_option()
        if option == 'c':
            create_supplier(inventory)
        elif option == 'r':
            remove_supplier(inventory)
        elif option == 'u':
            update_supplier(inventory)
        elif option == 's':
            search_supplier(inventory)
        elif option == 'l':
            print(inventory.list_suppliers())
        elif option == 'q':
            print('you quit successfully')
            done = True

def choose_option():
    """Choose an option for supplier management."""
    print("\nSupplier Management Options:")
    print("c: Create a new supplier")
    print("r: Remove a supplier")
    print("u: Update a supplier")
    print("s: Search for a supplier")
    print("l: List all suppliers")
    print("q: Quit")
    
    return input("Choose an option: ")

def create_supplier(inventory: Inventory):
    """Create a new supplier."""
    supplier_id = input("Enter supplier ID: ")
    name = input("Enter supplier name: ")
    contact_person = input("Enter contact person name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    
    supplier = Supplier(supplier_id, name, contact_person, email, phone, address)
    inventory.add_supplier(supplier)
    print(f"Supplier {supplier_id} created successfully")

def remove_supplier(inventory: Inventory):
    """Remove a supplier."""
    supplier_id = input("Enter supplier ID to remove: ")
    inventory.remove_supplier(supplier_id)
    print(f"Supplier {supplier_id} removed successfully")

def update_supplier(inventory: Inventory):
    """Update supplier information."""
    supplier_id = input("Enter supplier ID to update: ")
    supplier = inventory.get_supplier_by_id(supplier_id)
    
    if supplier:
        email = input("Enter new email (press enter to skip): ")
        phone = input("Enter new phone (press enter to skip): ")
        contact = input("Enter new contact person (press enter to skip): ")
        
        supplier.update_contact_info(
            email=email if email else None,
            phone=phone if phone else None,
            contact_person=contact if contact else None
        )
        print(f"Supplier {supplier_id} updated successfully")
    else:
        print(f"Supplier {supplier_id} not found")

def search_supplier(inventory: Inventory):
    """Search for a supplier."""
    supplier_id = input("Enter supplier ID to search: ")
    supplier = inventory.get_supplier_by_id(supplier_id)
    
    if supplier:
        print(supplier)
        print("\nSupplied products:")
        for product in supplier.products:
            print(product)
    else:
        print(f"Supplier {supplier_id} not found")
from inventory import Inventory
from category import Category

def category_management(inventory: Inventory):
    """Manage categories in the inventory. create, remove, list categories, and change VAT.
    
    Args:
        inventory (Inventory): the inventory
    """
    # Print all categories
    list_categories(inventory)
    
    done = False
    while not done:
        message = f"{'-'*106}\nTo create a category enter [c], to remove a category enter [r], to list all categories enter [l], to change VAT of a category enter [v], to quit category management enter [q]\n{'-'*106}"
        print(message)
        opt = choose_option()

        if opt == 'c':
            print("Create a category")
            create_category(inventory)
        elif opt == 'r':
            print('Remove a category')
            remove_category(inventory)
        elif opt == 'l':
            print('List all categories')
            list_categories(inventory)
        elif opt == 'v':
            print('Change VAT of a category')
            change_vat(inventory)
        elif opt == 'q':
            done = True
            print('You quit successfully')

def choose_option():
    """Choose an option to manage.
    
    Returns: opt (str) the chosen option
    """
    opt = input("Enter an option [c/r/l/v/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'crlvq':
            valid = True
        else:
            print("Option not valid")
            opt = input("Enter an option [c/r/l/v/q]: ")
    
    return opt

def create_category(inventory: Inventory):
    """Create a category.
    
    Args:
        inventory (Inventory): the inventory
    """
    name = input("Enter the category name: ")
    is_correct = False
    change_existing_category = 'n'
    while not is_correct:
        if inventory.search_category_by_name(name) is not None:
            print("Category ID already exists")
            change_existing_category = input("Do you want to change the vat of the existing category? [y/n]: ")
            if change_existing_category == 'y':
                is_correct = True
        else: 
            vat = float(input("Enter the VAT for the category: "))
            category = Category(name, vat)
            inventory.add_category(category)
            is_correct = True

    if change_existing_category == 'y':
        # change the existing category
        change_vat(inventory, name)
        
def remove_category(inventory: Inventory):
    """Remove a category.
    
    Args:
        inventory (Inventory): the inventory
    """
    name = input("Enter the category name: ")
    
    if name:
        inventory.remove_category(name)
    else:
        print("Category not found")

def change_vat(inventory: Inventory):
    """Change VAT of a category.
    
    Args:
        inventory (Inventory): the inventory
    """
    name = input("Enter the category name: ")
    category = inventory.search_category_by_name(name)
    if category is not None:
        new_vat = float(input("Enter the new VAT for the category: "))
        category.vat = new_vat
    else:
        print("Category not found")

def list_categories(inventory: Inventory):
    """List all categories.
    
    Args:
        inventory (Inventory): the inventory
    """
    res = "Categories in the inventory:\n"
    res = "-"*80 + '\n' + res + "-"*80 + "\n"
    for category in inventory.categories:
        res += str(category) + '\n'
    print(res)

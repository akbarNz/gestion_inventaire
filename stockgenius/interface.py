import sys
import os
import argparse

# Ajoute le chemin du dossier racine au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from stockgenius.init_state import init_state
from stockgenius.managment.category_management import category_management
from stockgenius.managment.order_management import order_management
from stockgenius.managment.product_management import product_management
from stockgenius.managment.supplier_management import supplier_management


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Parser for the data directory')

    # Add arguments
    parser.add_argument('data_dir', type=str, help='the directory of the data files to process')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    # Parse the arguments
    args = parser.parse_args()

    # Use the argument
    data_dir = args.data_dir
    
    # initial state of the inventory
    try:
        inventory = init_state(data_dir)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)
    
    # management interface

    w = "\nWelcome to stockGenius\n"
    s = '-'*len(w) + w + '-'*len(w)
    print(s)

    done = False
    
    while not done:
        message = (f"{'-'*106}\n"
                  f"to manage product enter [p], to manage orders enter [o], "
                  f"to manage categories enter [c], to manage suppliers enter [s], "
                  f"to quit enter [q]\n{'-'*106}")
        print(message)
        opt = choose_option()

        if opt == 'p':
            print("Products management")
            product_management(inventory)
        elif opt == 'o':
            print('Orders management')
            order_management(inventory)
        elif opt == 'c':
            print('Categories management')
            category_management(inventory)
        elif opt == 's':
            print('Suppliers management')
            supplier_management(inventory)
        elif opt == 'q':
            done = True
            generate_report(inventory)
            print('you quit successfully')

def choose_option():
    """Choose an option to manage.
    
    Returns: opt (str) the chosen option
    """
    opt = input("enter an option [p/o/c/s/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'pocsq':
            valid = True
        else:
            print("option not valid")
            opt = input("enter an option [p/o/c/s/q]: ")
    
    return opt   


def generate_report(inventory):
    report = {
        'number_of_products': len(inventory.products),
        'number_of_orders': len(inventory.orders),
        'sales_summary': inventory.generate_sales_summary(),
    }

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    report_file = os.path.join(output_dir, 'inventory_report.txt')

    with open(report_file, 'w') as f:
        for key, value in report.items():
            f.write(f"{key}: {value}\n")

    print(f"Report generated and saved to {report_file}")
    
if __name__ == '__main__':
    main()
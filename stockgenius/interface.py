import argparse
import os
from init_state import init_state
from managment.product_management import product_management
from managment.order_management import order_management
from managment.category_management import category_management

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

    print(inventory)

    done = False
    
    while not done:
        message = f"{'-'*106}\nto manage product enter [p], to manage orders enter [o], to manage categories enter [c], to quit enter [q]\n{'-'*106}"
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
        elif opt == 'q':
            done = True
            generate_report(inventory)
            print('you quit successefuly')

def choose_option():
    """Choose an option to manage.
    
    Returns: opt (str) the choosen option
    """
    opt = input("enter an option [p/o/c/q]: ")
    valid = False

    while not valid:
        if len(opt) == 1 and opt.lower() in 'pocq':
            valid = True
        else:
            print("option not valid")
            opt = input("enter an option [p/o/c/q]: ")
    
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
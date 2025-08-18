# StockGenius

A Python-based inventory management system that handles products, categories, orders, and suppliers.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/akbarNz/gestion_inventaire.git
cd gestion_inventaire
```

2. Set up the Python environment:
```bash
# Create and activate a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# Or
.\venv\Scripts\activate  # On Windows

# Install the package in development mode
pip install -e .
```

3. Set the PYTHONPATH:
```bash
# On Linux/Mac
export PYTHONPATH="${PYTHONPATH}:/path/to/gestion_inventaire"

# On Windows (PowerShell)
$env:PYTHONPATH += ";C:\path\to\gestion_inventaire"
```

## Running the Program

From the project root directory:
```bash
python3 stockgenius/interface.py stockgenius/data/
```

## Running Tests

To run all tests:
```bash
python3 -m unittest discover -s stockgenius/tests -v
```

To run specific test files:
```bash
# Run product tests
python3 -m unittest stockgenius/tests/test_product.py -v

# Run inventory tests
python3 -m unittest stockgenius/tests/test_inventory.py -v

# Run initialization tests
python3 -m unittest stockgenius/tests/test_init_state.py -v
```

## Project Structure

```
gestion_inventaire/
├── setup.py
├── README.md
└── stockgenius/
    ├── __init__.py
    ├── abstract_order.py      # New: Base class for orders
    ├── category.py
    ├── init_state.py
    ├── interface.py
    ├── inventory.py           # Modified: Added purchase order support
    ├── order_manager.py       # New: Handles automated purchases
    ├── product.py            # Modified: Added reorder points
    ├── purchase_order.py     # New: Purchase order implementation
    ├── sale_order.py         # New: Replaces order.py
    ├── supplier.py
    ├── data/
    │   ├── clothing.csv      # Modified: Updated with supplier_id
    │   ├── electronics.csv   # Modified: Updated with supplier_id
    │   ├── furniture.csv     # Modified: Updated with supplier_id
    │   └── suppliers.csv     # New: Supplier data
    ├── management/
    │   ├── __init__.py
    │   ├── category_management.py
    │   ├── order_management.py    # Modified: Handles both order types
    │   ├── product_management.py  # Modified: Added supplier support
    │   └── supplier_management.py # New: Supplier management
    └── tests/
        ├── __init__.py
        ├── test_abstract_order.py # New: Tests for base order class
        ├── test_category.py
        ├── test_inventory.py      # Modified: Added order tests
        ├── test_order_manager.py  # New: Tests for order manager
        ├── test_product.py        # Modified: Added supplier tests
        ├── test_purchase_order.py # New: Tests for purchase orders
        ├── test_sale_order.py     # New: Replaces test_order.py
        ├── test_supplier.py       # New: Tests for supplier class
        └── test_init_state.py     # Modified: Added supplier init
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests to ensure everything works
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Testing the Program

To test the **StockGenius** program, localy:

```sh
python3 stockgenius/interface.py stockgenius/data/
```

# First, make sure you're in the project root
cd /home/anzeyima/gestion_inventaire

# Set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/home/anzeyima/gestion_inventaire"

# Run tests with verbose output
python3 -m unittest stockgenius/tests/test_init_state.py -v
```



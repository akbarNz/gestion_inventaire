# StockGenius

A Python-based inventory management system that handles products, categories, orders, and suppliers.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gestion_inventaire.git
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
    ├── category.py
    ├── init_state.py
    ├── interface.py
    ├── inventory.py
    ├── order.py
    ├── product.py
    ├── supplier.py
    ├── data/
    │   ├── clothing.csv
    │   ├── electronics.csv
    │   ├── furniture.csv
    │   └── suppliers.csv
    ├── management/
    │   ├── __init__.py
    │   ├── category_management.py
    │   ├── order_management.py
    │   ├── product_management.py
    │   └── supplier_management.py
    └── tests/
        ├── __init__.py
        ├── test_category.py
        ├── test_inventory.py
        ├── test_order.py
        ├── test_product.py
        └── test_init_state.py
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



## Testing the Program

To test the **StockGenius** program, follow these steps:

### 1. Consolidate CSV Files
Run the following command to consolidate all CSV files in the `stockgenius/data/` directory into a single file named `consolidated_inventory.csv`:

```sh
python3 stockgenius/cli.py consolidate stockgenius/data/
```

### 2. Search by Product
Run the following command to search for a product by name in the consolidated inventory:

```sh
python3 stockgenius/cli.py search_product "ProductA"
```

### 3. Search by Category
Run the following command to search for products by category in the consolidated inventory:

```sh
python3 stockgenius/cli.py search_category "CategoryA"
```

### 4. Search by Price Range
Run the following command to search for products within a specified price range in the consolidated inventory:

```sh
python3 stockgenius/cli.py search_price_range 10 50
```

### 5. Generate Summary Report
Run the following command to generate a summary report and save it to the specified output file:

```sh
python3 stockgenius/cli.py generate_report output_file.txt
```
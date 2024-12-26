import click
import pandas as pd
from consolidate import consolidate_csv_files
from search import search_by_product, search_by_category, search_by_price_range
from report import generate_summary_report

@click.group()
def cli():
    pass

@click.command()
@click.argument('data_dir')
def consolidate(data_dir):
    df = consolidate_csv_files(data_dir)
    df.to_csv('consolidated_inventory.csv', index=False)
    click.echo('CSV files consolidated into consolidated_inventory.csv')

@click.command()
@click.argument('product_name')
def search_product(product_name):
    df = pd.read_csv('consolidated_inventory.csv')
    result = search_by_product(df, product_name)
    click.echo(result)

@click.command()
@click.argument('category')
def search_category(category):
    df = pd.read_csv('consolidated_inventory.csv')
    result = search_by_category(df, category)
    click.echo(result)

@click.command()
@click.argument('min_price', type=float)
@click.argument('max_price', type=float)
def search_price(min_price, max_price):
    df = pd.read_csv('consolidated_inventory.csv')
    result = search_by_price_range(df, min_price, max_price)
    click.echo(result)

@click.command()
@click.argument('output_file')
def report(output_file):
    df = pd.read_csv('consolidated_inventory.csv')
    generate_summary_report(df, output_file)
    click.echo(f'Summary report generated at {output_file}')

cli.add_command(consolidate)
cli.add_command(search_product)
cli.add_command(search_category)
cli.add_command(search_price)
cli.add_command(report)

if __name__ == '__main__':
    cli()
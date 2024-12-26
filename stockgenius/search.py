def search_by_product(df, product_name):
    return df[df['product'].str.contains(product_name, case=False)]

def search_by_category(df, category):
    return df[df['category'].str.contains(category, case=False)]

def search_by_price_range(df, min_price, max_price):
    return df[(df['price'] >= min_price) & (df['price'] <= max_price)]
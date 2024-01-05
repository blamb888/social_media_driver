import pandas as pd
import os
import random

def get_product_title_local_pinterest():
    # Load the data
    df = pd.read_csv('catalog/shopify_products_export_1.csv')

    # Remove rows with missing 'Title' or 'Handle'
    df = df.dropna(subset=['Title', 'Handle'])

    # Randomly select a row
    random_row = df.sample(n=1).iloc[0]

    # Get the title and URL from the random row
    product_title = random_row['Title']
    handle = random_row['Handle']
    base_url = os.getenv('SHOPIFY_SHOP_URL', 'https://tokyo-creative-collection.com')
    product_url = f"{base_url}/products/{handle}"

    return product_title, product_url

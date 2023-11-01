import pandas as pd
import random

def get_product_title_local():
    # Load the data
    df = pd.read_csv('catalog/facebook_catalog_final_refined.csv')

    # Randomly select a row
    random_row = df.sample(n=1)

    # Get the title and URL from the random row
    product_title = random_row['title'].values[0]
    etsy_url = random_row['link'].values[0]

    return product_title, etsy_url

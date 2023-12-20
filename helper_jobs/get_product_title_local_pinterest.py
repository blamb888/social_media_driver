import pandas as pd

def get_product_title_local(index):
    # Load the data
    df = pd.read_csv('catalog/facebook_catalog_final_refined.csv')

    # Ensure the index is within the bounds of the DataFrame
    if index >= len(df):
        print("Index out of bounds. Resetting to 0.")
        index = 0

    # Get the title and URL from the row at the specified index
    product_title = df.iloc[index]['title']
    etsy_url = df.iloc[index]['link']

    return product_title, etsy_url, index + 1

import pandas as pd

# Load the provided CSV
df_urls = pd.read_csv("facebook_catalog_updated_with_urls.csv")

# Modify the URLs in the 'link' column from the Etsy format to the required Facebook format
df_urls['link'] = df_urls['link'].str.replace('https://www.etsy.com', 'tokyocc.etsy.com', regex=False)

# Remove the query string from the 'link' column
df_urls['link'] = df_urls['link'].str.split('?').str[0]

# Save the updated data to a new CSV
output_file_path_urls = "facebook_catalog_with_updated_facebook_product_urls.csv"
df_urls.to_csv(output_file_path_urls, index=False)

print(output_file_path_urls)

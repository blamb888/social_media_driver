import pandas as pd

# Load the template CSV to determine the exact order of columns
df_template = pd.read_csv("catalog_products_template.csv")

# Load the current CSV
df_final = pd.read_csv("facebook_catalog_final.csv")

# Drop the specified columns
df_final_copy = df_final.drop(columns=['google_product_category_new', 'fb_product_category_new'], errors='ignore')

# Add "http://" to the beginning of each item in the "link" column
df_final_copy['link'] = 'http://' + df_final_copy['link']
df_final_copy.to_csv("facebook_catalog_final_no_categories.csv", index=False)
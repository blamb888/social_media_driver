import pandas as pd

# Load the provided CSV
df_updated = pd.read_csv("facebook_catalog_with_updated_facebook_product_urls.csv")

# Remove the rows corresponding to the specified products
df_updated = df_updated[~df_updated['title'].str.contains("Slaying with Sarcasm - Proficient in Vicious Mockery Gothic D&D Shirt", case=False)]
df_updated = df_updated[~df_updated['title'].str.contains("Red Dragon 'Roll for Initiative' Est 1974 Shower Curtain | D&D Inspired Bathroom Decor | Fantasy Role-Playing Game Home Accessory", case=False)]

# Save the updated data to a new CSV
output_file_path_removed_rows = "facebook_catalog_final.csv"
df_updated.to_csv(output_file_path_removed_rows, index=False)

output_file_path_removed_rows
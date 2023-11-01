from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
from dotenv import load_dotenv


def scrape_etsy_shop_urls_selenium(shop_url, num_pages=3):
    # Load environment variables from .env file
    load_dotenv()
    
    # Set up the web driver
    driver = webdriver.Chrome()  # If you've placed chromedriver elsewhere, use: webdriver.Chrome(executable_path='/path/to/chromedriver')
    product_urls = {}

    try:
        for page in range(1, num_pages + 1):
            driver.get(f"{shop_url}?page={page}#items")
            print(driver.current_url)

            # Wait for the page to load and extract product listings using the <a> tag with the 'title' attribute
            listings = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//a[@title]'))
            )
            print([l.get_attribute('href') for l in listings])

            for listing in listings:
                title = listing.get_attribute('title')
                link = listing.get_attribute('href')
                product_urls[title] = link

    finally:
        driver.quit()

    return product_urls

# Load your CSV
df = pd.read_csv("catalog/facebook_catalog_v6.csv")

# Scrape the product URLs
product_urls = scrape_etsy_shop_urls_selenium(os.environ['ETSY_SHOP_URL'])
print(product_urls)

# Match the URLs to the products in the CSV based on title
df['link'] = df['title'].map(product_urls)

# Save the updated CSV
df.to_csv("catalog/facebook_catalog_updated_with_urls.csv", index=False)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_product_title_from_etsy():
    etsy_url = input("Please enter the URL for the Etsy product you would like to make a social media post for: ")
    options = Options()
    options.add_argument("--headless")  # This line sets the browser to headless mode
    browser = webdriver.Chrome(options=options)
    browser.get(etsy_url)
    title_element = browser.find_element(By.XPATH,'//h1[@data-buy-box-listing-title="true"]')
    title = title_element.text
    browser.quit()  # This line closes the browser session
    return title

# Example usage:
product_title = get_product_title_from_etsy()
print(f'Product Title: {product_title}')

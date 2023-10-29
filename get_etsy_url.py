from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_etsy_url():
    etsy_url = input("Please enter the URL for the Etsy product you would like to make a social media post for: ")
    return etsy_url

def get_product_title(browser, etsy_url):
    browser.execute_script(f"window.open('{etsy_url}', '_blank');")
    browser.switch_to.window(browser.window_handles[1])
    title_element = browser.find_element(By.XPATH,'//h1[@data-buy-box-listing-title="true"]')
    title = title_element.text
    browser.quit()  # This line closes the browser session
    return title

# Example usage:
options = Options()
options.add_argument("--headless")  # This line sets the browser to headless mode
browser = webdriver.Chrome(options=options)
etsy_url = get_etsy_url()
product_title = get_product_title(browser, etsy_url)
print(f'Product Title: {product_title}')

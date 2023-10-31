import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def upload_image(browser, etsy_url):
    # Extract the product name from the Etsy URL
    product_name = re.search(r'listing/\d+/(.+?)(?:\?|$)', etsy_url).group(1)

    # Form the file path
    file_path = f'/home/unix_blamb/code/buffer_photos/{product_name}.png'

    # Find the file input element
    file_input = browser.find_element(By.XPATH, '//input[@data-testid="uploads-dropzone-input"]')

    # Send the file path to the file input element
    file_input.send_keys(file_path)
    
    # Wait for the image to be uploaded
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.XPATH, '//img[@data-testid="media-attachment-thumbnail"]'))
    )

# # Initialize the WebDriver
# browser = webdriver.Chrome()

# # Navigate to the page and perform the upload
# browser.get('url_of_the_page')
# upload_image(browser, 'https://www.etsy.com/listing/1476809576/slaying-with-sarcasm-proficient-in')

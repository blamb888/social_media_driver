import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_image_from_drive(browser, etsy_url):
    # Extract the product name from the Etsy URL
    product_name = re.search(r'listing/\d+/(.+?)(?:\?|$)', etsy_url).group(1)

    # Form the regex pattern to match the image file name in Google Drive
    pattern = re.compile(f'{product_name}\.png', re.IGNORECASE)

    # Click the "Select from Google Drive" button
    browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Select from Google Drive"]').click()

    # Click the "Buffer Photos" folder
    browser.find_element(By.XPATH, '//div[text()="Buffer Photos"]').click()

    # Wait for the thumbnail element to be present in the DOM
    WebDriverWait(browser, 25).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'thumbnail')]"))
    )

    # Iterate through images to find the matching one
    images = browser.find_elements(By.TAG_NAME, 'img')
    for image in images:
        src = image.get_attribute('src')
        if pattern.search(src):
            image.click()
            break

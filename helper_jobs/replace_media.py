from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helper_jobs.add_photo import upload_image  # assuming upload_image is defined in add_photo.py

def replace_media_with_image(browser, etsy_url):
    # Click the 'Replace link attachment with image or video' button
    replace_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="media-attachment-switch"]'))
    )
    replace_button.click()
    
    # Call the upload_image function to upload the image
    upload_image(browser, etsy_url)

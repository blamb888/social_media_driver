from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helper_jobs.add_photo import upload_image  # assuming upload_image is defined in add_photo.py
import time

def add_media(browser, etsy_url):
    print("Adding url...")
    post_textbox = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='composer-text-area']"))
    )
    post_textbox.send_keys(f'\n\n{etsy_url}\n')  # append the product URL on a new line

    # Wait for the 'Replace link attachment with image or video' button to appear
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-testid="media-attachment-switch"]'))
    )
    
    # Click the 'Replace link attachment with image or video' button
    replace_link_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="media-attachment-switch"]'))
    )
    replace_link_button.click()

    print("Waiting for image carousel to load...")
    time.sleep(10)  # Adjust the waiting time as necessary
    
    try:
        suggested_media_header = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Suggested media (8):']"))
        )
        if suggested_media_header:
            print("Suggested media found. Selecting first option.")
        first_option_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='_suggestionsScrollContainer_13oy6_121']/button[1]"))
        )
        first_option_button.click()
    except:
        print("No suggested media found. Uploading image...")
        # Select image from Google Drive
        upload_image(browser, etsy_url)

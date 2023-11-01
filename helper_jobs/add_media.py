from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from helper_jobs.add_photo import upload_image  # assuming upload_image is defined in add_photo.py
import time
import random

def add_media(browser, etsy_url):
    print("Adding url...")
    post_textbox = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='composer-text-area']"))
    )

    post_textbox.send_keys(f'\n\n{etsy_url}\n')  # append the product URL on a new line

    try:
        # Wait for the 'Replace link attachment with image or video' button to appear
        replace_link_button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="media-attachment-switch"]'))
        )
        replace_link_button.click()
    except TimeoutException:
        print("The 'Replace link attachment with image or video' button did not appear or was not clickable.")


    print("Waiting for image carousel to load...")
    time.sleep(10)  # Adjust the waiting time as necessary
    
    try:
        suggested_media_header = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Suggested media')]"))
        )
        if suggested_media_header:
            print("Suggested media found.")
            image_buttons = browser.find_elements(By.XPATH, "//div[contains(@class, '_suggestionsScrollContainer')]/button")
            total_images = len(image_buttons)
            if total_images > 1:
                random_index = random.randint(1, total_images - 1)  # Avoid the last image
                print(f"Selecting image {random_index}.")
                image_buttons[random_index - 1].click()  # Lists are 0-indexed, so we subtract 1
            else:
                print("Only one image found. Selecting it.")
                image_buttons[0].click()
    except:
        print("No suggested media found. Uploading image...")
        # Select image from Google Drive
        upload_image(browser, etsy_url)

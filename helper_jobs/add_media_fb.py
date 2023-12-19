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

    print("Waiting for image carousel to load...")
    time.sleep(10)  # Adjust the waiting time as necessary

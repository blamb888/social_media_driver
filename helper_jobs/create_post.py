from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.ai_assistant_interaction import interact_with_ai_assistant
from helper_jobs.add_media import add_media
from helper_jobs.logout import logout
import time

def create_post(browser, title, etsy_url):
    print("Creating post...")

    # Wait for JavaScript and rendering
    time.sleep(5)  # Wait for the JavaScript to load

    # Handle popup
    try:
        popup_close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-0f60d048']"))  
        )
        popup_close_button.click()
        print("Popup closed.")
    except Exception as e:
        print(f"No popup appeared: {e}")

    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Create Post')]]"))
    )
    create_post_button.click()
    
    # Interact with AI Assistant
    interact_with_ai_assistant(browser, title)

    # Add media
    add_media(browser, etsy_url)
        
    # Click 'Add to Queue'
    add_to_queue_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button/div[text()='Add to Queue']"))
    )
    add_to_queue_button.click()
    print("Clicking add to queue button...")

    time.sleep(5)  # Wait for post to be queued

    logout(browser)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.ai_assistant_interaction import interact_with_ai_assistant
from helper_jobs.handle_media import add_media

import time

def create_post(browser, title, etsy_url):
    print("Creating post...")

    # Handle popup
    try:
        popup_close_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-0f60d048']"))  
        )
        popup_close_button.click()
        print("Popup closed.")
    except:
        print("No popup appeared.")
    
    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Create Post')]]"))
    )
    create_post_button.click()
    
    # Click on the 'Use the AI Assistant' button
    interact_with_ai_assistant(browser, title)

    
    # Handle new popup
    try:
        new_popup_close_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))  
        )
        new_popup_close_button.click()
        print("New popup closed.")
    except:
        print("No new popup appeared.")
    
    # Click on the 'Insert' button
    insert_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Insert']"))
    )
    insert_button.click()
        
    # Handle new popup
    try:
        new_popup_close_button = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-33adcb58']"))  
        )
        new_popup_close_button.click()
        print("New popup closed.")
    except:
        print("No new popup appeared.")
    
    close_button = browser.find_element(By.XPATH, '//div[@data-testid="composer-sidepanel"]//div')
    close_button.click()
    print("AI Assistant closed.")
    
    # Add media
    add_media(browser, etsy_url)
        
    # Click on the 'Customize for each network' button
    customize_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Customize for each network']"))
    )
    customize_button.click()
    print("Clicking customize for each network button...")
    
    # Add a wait time
    time.sleep(25)  # waits for 25 seconds
        
    # Check if 'Add to Queue' button is disabled
    add_to_queue_button = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button/div[text()='Add to Queue']"))
    )
    add_to_queue_button.click()
    print("Clicking add to queue button...")
    
    # Add a wait time
    time.sleep(25)  # waits for 25 seconds

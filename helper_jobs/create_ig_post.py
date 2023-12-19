from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.ai_assistant_interaction import interact_with_ai_assistant
from helper_jobs.add_media_ig import add_media
from helper_jobs.logout import logout

import time

def create_post(browser, title, etsy_url):
    print("Creating post...")

    # Handle initial popup
    try:
        popup_close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-0f60d048']"))  
        )
        popup_close_button.click()
        print("Popup closed.")
    except:
        print("No popup appeared.")
    
    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Create Post')]]"))
    )
    create_post_button.click()
    
    # Use the AI Assistant
    interact_with_ai_assistant(browser, title)
    
    # Handle new popup after AI Assistant interaction
    try:
        new_popup_close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Close']"))  
        )
        new_popup_close_button.click()
        print("New popup closed.")
    except:
        print("No new popup appeared.")
    
    # Toggle off Facebook posts
    facebook_toggle_button_xpath = "//button[@name='facebook-profile-button' and @aria-checked='true']"
    facebook_toggle_buttons = browser.find_elements(By.XPATH, facebook_toggle_button_xpath)
    if facebook_toggle_buttons:
        try:
            facebook_toggle_buttons[0].click()
            print("Facebook posts toggled off.")
        except Exception as e:
            print("Error clicking Facebook toggle button, trying JavaScript:", e)
            browser.execute_script("arguments[0].click();", facebook_toggle_buttons[0])
    else:
        print("Facebook posts already toggled off or button not found.")
    
    # Add media
    add_media(browser, etsy_url)
        
    # Either click 'Customize for each network' or 'Add to Queue' depending on availability
    try:
        customize_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Customize for each network']"))
        )
        customize_button.click()
        print("Clicking customize for each network button...")
        time.sleep(15)  # waits for 15 seconds
    except:
        print("'Customize for each network' button not found. Ready to add to queue.")

    add_to_queue_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button/div[text()='Add to Queue']"))
    )
    add_to_queue_button.click()
    print("Clicking add to queue button...")

    time.sleep(15)

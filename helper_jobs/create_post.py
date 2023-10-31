from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def create_post(browser, title, etsy_url):
    print("Creating post...")
    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Create Post')]"))
    )
    create_post_button.click()
    
    # Click on the 'Use the AI Assistant' button
    ai_assistant_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='ai-assistant-placeholder-button']"))
    )
    ai_assistant_button.click()
    
    # Enter the product title into the AI Assistant's text box
    ai_assistant_textbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@id='prompt']"))
    )
    ai_assistant_textbox.send_keys(title)
    
    # Click on the 'Generate' button
    generate_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    generate_button.click()

    # Wait for the 'Still working...' text to disappear
    WebDriverWait(browser, 60).until_not(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Still working...')]"))
    )

    print("Inserting AI generated post")
    time.sleep(3)  # wait for 3 seconds

    # Click on the 'Insert' button
    insert_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Insert']"))
    )
    insert_button.click()

    print("Inserting product URL to post")
    post_textbox = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='What would you like to share?']"))
    )
    post_textbox.send_keys(f'\n{etsy_url}')  # append the product URL on a new line

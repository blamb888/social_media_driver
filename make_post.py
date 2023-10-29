from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_post(browser, title):
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

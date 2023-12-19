from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def interact_with_ai_assistant(browser, title):
    # Click on the 'Use the AI Assistant' button using JavaScript
    ai_assistant_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='ai-assistant-placeholder-button']"))
    )
    browser.execute_script("arguments[0].click();", ai_assistant_button)
    
    # Enter the product title into the AI Assistant's text box
    ai_assistant_textbox = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@id='prompt']"))
    )
    ai_assistant_textbox.send_keys(title)
    
    # Click on the 'Generate' button
    generate_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    generate_button.click()

    # Wait for the 'Still working...' text to disappear
    WebDriverWait(browser, 60).until_not(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Still working...')]"))
    )
    
    # Click on the 'More Casual' button
    more_casual_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='More Casual']"))
    )
    more_casual_button.click()
    
    # Wait for the 'Still working...' text to disappear
    WebDriverWait(browser, 60).until_not(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Unleashing AI')]"))
    )

    print("Inserting AI generated post")
    # XPath to find the button using its class attributes
    button_xpath = "//button[@type='button' and contains(@class, 'sc-cEEJxU') and contains(@class, 'llKORI')]"

    try:
        # Wait until the button is clickable
        insert_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )
        insert_button.click()
        print("Button clicked successfully.")
    except Exception as e:
        print(f"Error clicking the button: {e}")

    time.sleep(3)  # wait for 3 seconds

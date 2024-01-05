from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def interact_with_ai_assistant(browser, product_title):
    # Click on the 'AI Assistant' button
    ai_assistant_button_xpath = "//button[@id='button-ai-assistant-v2']"
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ai_assistant_button_xpath))
    ).click()
    print("AI Assistant button clicked.")
    
    # let's wait a little bit
    time.sleep(5)

    # Click on 'Write more' button
    write_more_button_xpath = "//button[@data-testid='ai-assistant-write-more-button']"
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, write_more_button_xpath))
    ).click()
    print("Write more button clicked.")

    # Enter the product product_title into the AI Assistant's text box
    ai_assistant_textbox_xpath = "//textarea[@id='prompt']"
    ai_assistant_textbox = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ai_assistant_textbox_xpath))
    )
    ai_assistant_textbox.send_keys(product_title)
    print("Product product_title entered into AI Assistant.")

    # Click on the 'Generate' button
    generate_button_xpath = "//button[@data-testid='ai-assistant-generate-button']"
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, generate_button_xpath))
    ).click()
    print("Generate button clicked.")

    # Wait for the AI Assistant to generate the text
    time.sleep(15)  # Adjust this wait time based on how long the generation usually takes

    # Click on the 'Shorten' button
    shorten_button_xpath = "//button[@data-testid='ai-assistant-fine-tuning-shorten-button']"
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, shorten_button_xpath))
    ).click()
    print("Shorten button clicked.")

    # Wait for the text to be shortened
    time.sleep(5)

    # Click on the 'Insert' button
    insert_button_xpath = "//button[text()='Insert']"
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, insert_button_xpath))
    ).click()
    print("Insert button clicked.")

    time.sleep(3)  # wait for 3 seconds

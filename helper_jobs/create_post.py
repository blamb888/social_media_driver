from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.select_image_from_drive import select_image_from_drive
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
    ai_assistant_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='ai-assistant-placeholder-button']"))
    )
    ai_assistant_button.click()
    
    # Enter the product title into the AI Assistant's text box
    ai_assistant_textbox = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@id='prompt']"))
    )
    ai_assistant_textbox.send_keys(title)
    
    # Click on the 'Generate' button
    generate_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    generate_button.click()

    # Wait for the 'Still working...' text to disappear
    WebDriverWait(browser, 60).until_not(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Still working...')]"))
    )

    print("Inserting AI generated post")
    time.sleep(3)  # wait for 3 seconds
    
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

    post_textbox = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='composer-text-area']"))
    )
    post_textbox.send_keys(f'\n\n{etsy_url}\n')  # append the product URL on a new line

    # Check for Suggested media carousel
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
        print("No suggested media found. Selecting image from Google Drive.")
        
        # Select image from Google Drive
        select_image_from_drive(browser, etsy_url)
        
    # # Click on the 'Customize for each network' button
    # customize_button = WebDriverWait(browser, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[text()='Customize for each network']"))
    # )
    # customize_button.click()
    # print("Clicking customize for each network button...")
        
    # Check if 'Add to Queue' button is disabled
    add_to_queue_button = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button/div[text()='Add to Queue']"))
    )
    add_to_queue_button.click()
    
    # button_disabled = WebDriverWait(browser, 30).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@data-testid='stacked-save-buttons-section'][@data-disabled='true']"))
    # )

    # if button_disabled:
    #     print("Posts not ready, selecting images now...")
        
    #     # Locate the div elements
    #     div_elements = browser.find_elements(By.XPATH,"//div[contains(@class, 'standard-composer')]")
    #     print(f'Found {len(div_elements)} div elements.')

    #     # Iterate through each div element and click to expand them
    #     for div in div_elements:
    #         div.click()
    #         print("Expanding div...")
    #         # Wait for the suggestions to load
    #         WebDriverWait(browser, 30).until(
    #             EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_thumbnailContainer')]"))
    #         )
    #         # Click the first suggested image
    #         first_suggested_image = browser.find_element(By.XPATH, "(//button[contains(@class, '_thumbnailContainer')])[1]")
    #         first_suggested_image.click()
    #         print("Selected first suggested image...")
        
    #     # Keep browser open for 10 seconds
    #     time.sleep(10)
    # else:
    #     print("Adding Posts to Queue now...")
    #     add_to_queue_button.click()
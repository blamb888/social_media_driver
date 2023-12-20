from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.ai_assistant_interaction import interact_with_ai_assistant
from helper_jobs.add_media_ig import add_media

import time

def create_pinterest_post(browser, title, etsy_url):
    print("Creating Pinterest post...")

    # Handle initial popup
    try:
        popup_close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-0f60d048']"))
        )
        popup_close_button.click()
        print("Popup closed.")
    except Exception as e:
        print("No popup appeared or error closing it:", e)

    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Create Post')]]"))
    )
    create_post_button.click()

    # Disable Instagram and Facebook channels
    # XPath for the first Facebook button
    facebook_button1_xpath = "//button[@name='facebook-profile-button' and @aria-label='Tokyo Creative Collection facebook Page' and @aria-checked='true']"

    try:
        facebook_button1 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, facebook_button1_xpath))
        )
        facebook_button1.click()
        print("First Facebook channel toggled off.")
    except Exception as e:
        print("Error clicking the first Facebook channel button:", e)

    # XPath for the second Facebook button
    facebook_button2_xpath = "//button[@name='facebook-profile-button' and @aria-label='Tokyo CC facebook Page' and @aria-checked='true']"

    try:
        facebook_button2 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, facebook_button2_xpath))
        )
        facebook_button2.click()
        print("Second Facebook channel toggled off.")
    except Exception as e:
        print("Error clicking the second Facebook channel button:", e)
        
    time.sleep(3)
    
    # Toggle off Instagram posts
    instagram_toggle_buttons_xpath = "//button[@name='instagram-profile-button' and @aria-checked='true']"
    instagram_toggle_buttons = browser.find_elements(By.XPATH, instagram_toggle_buttons_xpath)
    for button in instagram_toggle_buttons:
        try:
            button.click()
            print("Instagram post toggled off.")
        except Exception as e:
            print("Error clicking Instagram toggle button, trying JavaScript:", e)
            browser.execute_script("arguments[0].click();", button)

    # Select Pinterest Channel
    try:
        pinterest_channel_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='_profilePicture_1vb8p_53' and contains(@style, 'https://i.pinimg.com')]"))
        )
        pinterest_channel_button.click()
        print("Pinterest channel selected.")
    except Exception as e:
        print("Error selecting Pinterest channel:", e)

    # Select Board 'Accessories'
    try:
        accessories_board = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Accessories')]"))
        )
        accessories_board.click()
        print("Accessories board selected.")
    except Exception as e:
        print("Error selecting Accessories board:", e)

    # Insert Post, Add URL, Pick Picture
    add_media(browser, etsy_url)

    # Delete URL from Post Area
    try:
        post_textarea_xpath = "//textarea[@data-testid='composer-text-area']"  # Adjust this XPath to correctly identify the post text area
        post_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, post_textarea_xpath))
        )
        post_textarea.clear()
        print("URL cleared from post area.")
    except Exception as e:
        print("Error clearing URL from post area:", e)
        
    # Use the AI Assistant and click 'Shorten'
    interact_with_ai_assistant(browser, title)

    # Add URL to the 'destinationLink' field
    try:
        url_input_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "destinationLink"))
        )
        url_input_field.clear()  # Clear any existing text
        url_input_field.send_keys(etsy_url)
        print("URL added to destination link field.")
    except Exception as e:
        print("Error adding URL to destination link field:", e)

    # Add Title to the 'pinTitle' field
    try:
        title_input_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.NAME, "pinTitle"))
        )
        title_input_field.clear()  # Clear any existing text
        title_input_field.send_keys(title)
        print("Title added to pin title field.")
    except Exception as e:
        print("Error adding title to pin title field:", e)

    # Add to Queue
    try:
        add_to_queue_button = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button/div[text()='Add to Queue']"))
        )
        add_to_queue_button.click()
        print("Post added to queue.")
    except Exception as e:
        print("Error adding post to queue:", e)

    time.sleep(15)


from helper_jobs.disable_channels import disable_channels
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.ai_assistant_interaction_pinterest import interact_with_ai_assistant
from helper_jobs.add_media_ig import add_media
from helper_jobs.trim_posts import trim_post_content
from selenium.common.exceptions import TimeoutException
import time

def create_post(browser, title, etsy_url):
    print("Creating Pinterest post...")

    # Handle initial popup
    try:
        popup_close_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='pendo-close-guide-0f60d048']"))
        )
        if popup_close_button.is_displayed():
            popup_close_button.click()
            print("Popup closed.")
        else:
            print("Popup not displayed.")
    except Exception as e:
        print("No popup appeared or error closing it:", e)

    # Click on the 'Create Post' button
    create_post_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[contains(text(), 'Create Post')]]"))
    )
    create_post_button.click()

    # Disable Instagram and Facebook channels
    disable_channels(browser, "facebook1", "facebook2", "instagram1", "instagram2")
    
    time.sleep(5)

    # Select Pinterest Channel
    try:
        pinterest_channel_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='switch' and @name='pinterest-profile-button' and @aria-label='tokyo_creative_collection pinterest Business']"))
        )
        pinterest_channel_button.click()
        print("Pinterest channel selected.")
    except Exception as e:
        print("Error selecting Pinterest channel:", e)

    # Select Board 'Nerdy Stuff'
    try:
        nerdy_stuff_board = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Nerdy Stuff')]"))
        )
        nerdy_stuff_board.click()
        print("Nerdy Stuff board selected.")
    except Exception as e:
        print("Error selecting Nerdy Stuff board:", e)

    # Insert Post, Add URL, Pick Picture
    add_media(browser, etsy_url)

    # Delete URL from Post Area
    try:
        post_textarea_xpath = "//div[@data-testid='composer-text-area']"
        post_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, post_textarea_xpath))
        )
        # Clearing content of a contenteditable div
        browser.execute_script("arguments[0].innerText = '';", post_textarea)
        print("URL cleared from post area.")
    except TimeoutException:
        print("Timeout while trying to clear URL from the post area. Check if the post text area is visible.")
    except Exception as e:
        print("Error clearing URL from post area:", e)

    # Wait for a moment before using AI Assistant
    time.sleep(5)
        
    # Use the AI Assistant and click 'Shorten'
    try:
        interact_with_ai_assistant(browser, title)
        print("AI Assistant interaction successful.")
    except TimeoutException as e:
        print("Timeout while trying to interact with AI Assistant. Check if the AI Assistant button is visible and clickable.")
        print("Error:", e)
    except Exception as e:
        print("Error interacting with AI Assistant:", e)

    # Trimming post content if necessary
    trim_post_content(browser)

    # Add URL to the 'destinationLink' field
    try:
        url_input_xpath = "//input[@aria-labelledby='destinationLink']"
        url_input_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, url_input_xpath))
        )
        url_input_field.clear()
        url_input_field.send_keys(etsy_url)
        print("URL added to destination link field.")
    except Exception as e:
        print("Error adding URL to destination link field:", e)

    # Add Title to the 'pinTitle' field
    try:
        title_input_xpath = "//input[@aria-labelledby='pinTitle']"
        title_input_field = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, title_input_xpath))
        )
        title_input_field.clear()
        title_input_field.send_keys(title)
        print("Title added to pin title field.")
    except Exception as e:
        print("Error adding title to pin title field:", e)

    # Wait a moment before proceeding to add the post to the queue
    time.sleep(5)

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

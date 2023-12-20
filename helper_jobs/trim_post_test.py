from helper_jobs.disable_channels import disable_channels
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Manually inserting a long string into the text area for testing
    post_textarea_xpath = "//div[@data-testid='composer-text-area']"
    try:
        post_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, post_textarea_xpath))
        )
        long_string = "A" * 600  # Create a string with 600 characters
        browser.execute_script("arguments[0].innerText = arguments[1];", post_textarea, long_string)
        print("Long string inserted into post area.")
    except Exception as e:
        print("Error inserting long string into post area:", e)
    
    # Trimming post content if necessary
    trim_post_content(browser)

    time.sleep(15)


from helper_jobs.get_product_title_local import get_product_title_local
from helper_jobs.initialize_browser import initialize_browser
from helper_jobs.login import login
from helper_jobs.logout import logout
from helper_jobs.create_fb_post import create_post  # Assuming this function is for Facebook posts
from selenium.webdriver.common.by import By
import traceback
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_POSTS = 100

def get_scheduled_post_count(browser):
    browser.get('https://publish.buffer.com/calendar/week')
    try:
        wait = WebDriverWait(browser, 10)  # wait for a maximum of 10 seconds
        
        # XPath modified to target the third element in the sequence
        post_count_element_xpath = "//*[@id='root']/div/div[1]/div[1]/div[1]/div/ul[2]/div[4]/div/li/span"
        post_count_element = wait.until(EC.presence_of_element_located((By.XPATH, post_count_element_xpath)))
        post_count = int(post_count_element.text) if post_count_element.text else 0
        return post_count
    except Exception as e:
        print(f"Error while trying to get the post count: {e}")
        return None

browser = initialize_browser()

try:
    login(browser)

    # Ensure you're on the correct page
    if browser.current_url != 'https://publish.buffer.com/calendar/week':
        browser.get('https://publish.buffer.com/calendar/week')
    if browser.current_url != 'https://publish.buffer.com/calendar/week':
        raise Exception("Navigation to Buffer calendar page failed")
    

    while True:
        current_post_count = get_scheduled_post_count(browser)
        if current_post_count is None:
            raise Exception("Could not retrieve post count.")

        if current_post_count < MAX_POSTS:
            product_title, etsy_url = get_product_title_local()
            print(f'Product Title: {product_title}')
            create_post(browser, product_title, etsy_url)
            print("Post created successfully!")
        else:
            print("Maximum number of posts already scheduled.")
            break  # Exit the loop when MAX_POSTS is reached

        time.sleep(5)  # Short delay to prevent overwhelming the server

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())

finally:
    logout(browser)  # Logout after all operations are done
    browser.quit()

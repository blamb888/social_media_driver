from helper_jobs.get_product_title_local import get_product_title_local
from helper_jobs.initialize_browser import initialize_browser
from helper_jobs.login import login
from helper_jobs.logout import logout
from helper_jobs.create_post import create_post
from helper_jobs.disable_pinterest_channel import disable_pinterest_channel
import traceback
import time

browser = initialize_browser()

try:
    product_title, etsy_url = get_product_title_local()
    print(f'Product Title: {product_title}')

    login(browser)

    # Check if the current URL is the desired one
    if browser.current_url != 'https://publish.buffer.com/calendar/week':
        # If not, navigate to the desired URL
        browser.get('https://publish.buffer.com/calendar/week')

    # Check again if you are on the correct page
    if browser.current_url == 'https://publish.buffer.com/calendar/week':
        print("Logged into Buffer and navigated to the calendar successfully!")
    else:
        print("Failed to navigate to the calendar page.")
        
    # disable_pinterest_channel(browser)
    # print("Pinterest channel disabled.")
    
    # Add a wait time
    # time.sleep(25)  # waits for 25 seconds
    
    create_post(browser, product_title, etsy_url)
    print("Post created successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())  # This will print the stack trace

finally:
    # Close the browser
    browser.quit()

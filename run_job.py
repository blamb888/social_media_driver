from helper_jobs.get_product_title import get_product_title
from helper_jobs.initialize_browser import initialize_browser
from helper_jobs.login import login
from helper_jobs.logout import logout
from helper_jobs.create_post import create_post
import traceback

browser = initialize_browser()

try:
    product_title, etsy_url = get_product_title()
    print(f'Product Title: {product_title}')

    login(browser)
    if browser.current_url == 'https://publish.buffer.com/calendar/week':
        print("Logged into Buffer successfully!")
        create_post(browser, product_title, etsy_url)

    logout(browser)
    if "login" in browser.current_url:
        print("Logged out of Buffer successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())  # This will print the stack trace

finally:
    # Close the browser
    browser.quit()

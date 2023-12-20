import pandas as pd
import traceback
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper_jobs.get_product_title_local import get_product_title_local
from helper_jobs.initialize_browser import initialize_browser
from helper_jobs.login import login
from helper_jobs.logout import logout
from helper_jobs.trim_post_test import create_post

MAX_POSTS = 100

def get_scheduled_post_count(browser):
    browser.get('https://publish.buffer.com/calendar/month')
    try:
        wait = WebDriverWait(browser, 10)
        post_count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[1]/div/ul[2]/div[1]/div/li/span")))
        post_count = int(post_count_element.text) if post_count_element.text else 0
        return post_count
    except Exception as e:
        print(f"Error while trying to get the post count: {e}")
        return None

def get_product_title_local(index):
    df = pd.read_csv('catalog/facebook_catalog_final_refined.csv')
    if index >= len(df):
        print("Index out of bounds. Resetting to 0.")
        index = 0
    product_title = df.iloc[index]['title']
    etsy_url = df.iloc[index]['link']
    return product_title, etsy_url, index + 1

browser = initialize_browser()

try:
    login(browser)
    product_index = 0

    while True:
        current_post_count = get_scheduled_post_count(browser)
        if current_post_count is None:
            raise Exception("Could not retrieve post count.")

        if current_post_count < MAX_POSTS:
            product_title, etsy_url, product_index = get_product_title_local(product_index)
            print(f'Product Title: {product_title}')
            create_post(browser, product_title, etsy_url)
            print("Post created successfully!")
        else:
            print("Maximum number of posts already scheduled.")
            break

        time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")
    print(traceback.format_exc())

finally:
    logout(browser)
    browser.quit()

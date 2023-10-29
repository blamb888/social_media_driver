from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from get_etsy_url import get_product_title_from_etsy

# Load environment variables from .env file
load_dotenv()

# Configure the headless browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")  # specify a port

browser = webdriver.Chrome(options=options)

try:
    # Grab Etsy Information
    title = get_product_title_from_etsy()

    
    # Navigate to the Buffer login page
    print("Navigating to Buffer login page...")
    browser.get('https://login.buffer.com/login?plan=free&cycle=year')

    # Attempt to find the email and password fields by common attribute names
    print("Filling in login form...")
    email_field = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    password_field = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    # Fill in the login form and submit
    email_field.send_keys(os.environ['BUFFER_EMAIL'])
    password_field.send_keys(os.environ['BUFFER_PASSWORD'])
    password_field.submit()

    # Check for successful login by verifying URL redirection
    if browser.current_url == 'https://publish.buffer.com/calendar/week':
        print("Logged into Buffer successfully!")

    # Logout
    
    # Click on the menu to reveal the logout button
    print("Clicking on the menu to reveal the logout button...")
    menu_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[descendant::div[contains(text(), 'Logout')]]"))
    )
    menu_button.click()

    # Wait for the logout button to become clickable
    print("Waiting for the logout button to become clickable...")
    logout_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Logout')]"))
    )

    # Click on the logout button
    print("Clicking on the logout button to logout...")
    logout_button.click()


    # Check for successful logout by verifying redirection to the login page
    if "login" in browser.current_url:
        print("Logged out of Buffer successfully!")

finally:
    # Close the browser
    browser.quit()

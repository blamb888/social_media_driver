from selenium.webdriver.common.by import By
import os

def login(browser):
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

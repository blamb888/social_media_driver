from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

def initialize_browser():
    # Load environment variables from .env file
    load_dotenv()

    # Configure the headless browser
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")  # specify a port

    browser = webdriver.Chrome(options=options)
    return browser

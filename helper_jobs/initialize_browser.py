from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

def initialize_browser():
    # Configure the headless browser
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")  # Set the desired window size
    # options.add_argument("--remote-debugging-port=9222")  # specify a port

    browser = webdriver.Chrome(options=options)
    return browser

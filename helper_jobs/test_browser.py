from selenium import webdriver

def open_browser():
    browser = webdriver.Chrome()
    return browser

# Call the function to open the browser
browser_instance = open_browser()

# Pause the script until you press Enter in the console
input("Press Enter to close the browser...")

# Optionally, close the browser programmatically
browser_instance.quit()

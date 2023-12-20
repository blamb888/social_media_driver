from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_tags(browser):
    print("Adding tags...")

    # Click on 'Add Tags' button
    try:
        add_tags_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Add Tags']"))
        )
        add_tags_button.click()
        print("Opened the tags dropdown.")
    except Exception as e:
        print("Error opening tags dropdown:", e)
        return

    # Select the specific tag
    try:
        specific_tag = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='https://www.etsy.com/shop/TokyoCC']"))
        )
        specific_tag.click()
        print("Tag selected.")
    except Exception as e:
        print("Error selecting the tag:", e)
        return

    # Close the accordion
    try:
        close_accordion_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//svg[@class='Icon__StyledIcon-bufferapp-ui__sc-dbjb4v-0 jDIXHd']"))
        )
        close_accordion_button.click()
        print("Accordion closed.")
    except Exception as e:
        print("Error closing the accordion:", e)

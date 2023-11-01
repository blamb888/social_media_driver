from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def disable_pinterest_channel(browser):
    # Click 'All channels'
    all_channels_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[text()="All channels"]'))
    )
    all_channels_button.click()

    # Click to turn off Pinterest channel
    pinterest_channel_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="64734f324aa145702bac7397"]/div/p/span[1]'))
    )
    pinterest_channel_button.click()

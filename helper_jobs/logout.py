from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logout(browser):
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

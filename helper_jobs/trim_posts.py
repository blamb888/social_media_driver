from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def trim_post_content(browser):
    try:
        post_textarea_xpath = "//div[@data-testid='composer-text-area']"
        post_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, post_textarea_xpath))
        )

        # Click on the text area to focus
        post_textarea.click()

        # Get the current text from the text area
        post_text = post_textarea.text

        # Trim the text if it exceeds 500 characters
        if len(post_text) > 500:
            trimmed_text = post_text[:497] + "..."
            # Select all text (Ctrl+A) and replace it with the trimmed text
            post_textarea.send_keys(Keys.CONTROL + "a")
            post_textarea.send_keys(trimmed_text)
            print("Post content trimmed to 500 characters.")
        else:
            print("Post content is within the character limit.")

    except TimeoutException:
        print("Timeout while trying to access the post text area.")
    except Exception as e:
        print("Error while trimming post content:", e)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def trim_post_content(browser):
    post_textarea_xpath = "//div[@data-testid='composer-text-area']"
    try:
        # Retrieve the text area element
        post_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, post_textarea_xpath))
        )

        # Get the current text from the text area and trim if necessary
        trimmed_text = browser.execute_script("""
            var textArea = arguments[0];
            var text = textArea.innerText;
            if (text.length > 500) {
                return text.substring(0, 497) + "...";
            } else {
                return text;
            }
        """, post_textarea)

        # Set the trimmed text back to the text area
        browser.execute_script("arguments[0].innerText = arguments[1];", post_textarea, trimmed_text)
        print("Post content checked and trimmed if necessary.")

    except TimeoutException:
        print("Timeout while trying to access the post text area.")
    except Exception as e:
        print("Error while trimming post content:", e)

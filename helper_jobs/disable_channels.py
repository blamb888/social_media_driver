from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def disable_channels(browser, *channels):
    if not channels:
        print("No channels disabled")
        return

    channel_selectors = {
        "facebook1": "//button[@name='facebook-profile-button' and @aria-label='Tokyo Creative Collection facebook Page' and @aria-checked='true']",
        "facebook2": "//button[@name='facebook-profile-button' and @aria-label='Tokyo CC facebook Page' and @aria-checked='true']",
        "instagram1": "//button[@role='switch' and @name='instagram-profile-button' and @aria-label='starry_b_eats instagram Business' and @aria-checked='true']",
        "instagram2": "//button[@role='switch' and @name='instagram-profile-button' and @aria-label='tokyo_creative_collection instagram Business' and @aria-checked='true']",
        "pinterest": "//span[contains(@style, 'background-image: url(\"https://i.pinimg.com/600x600_R/d3/39/8d/d3398dd2dfc45c4b3004dee44addf152.jpg\");')]"
    }

    for channel in channels:
        if channel in channel_selectors:
            try:
                button = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, channel_selectors[channel]))
                )
                button.click()
                print(f"{channel.capitalize()} channel toggled off.")
            except Exception as e:
                print(f"Error clicking the {channel} channel button:", e)
        else:
            print(f"Channel '{channel}' not recognized or not provided in channel_selectors.")

# Example usage:
# disable_channels(browser, "facebook1", "instagram1", "pinterest")


import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# Note: You must run Chrome with a specific user profile flag to bypass the Google login screen
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

driver.get("https://www.youtube.com/feed/history")
time.sleep(10) 

print("Looking for today's videos...")
first_section = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-item-section-renderer"))
)

video_elements = first_section.find_elements(By.CSS_SELECTOR, "div#contents a[href^='/watch']")

urls = []
for el in video_elements:
    url = el.get_attribute("href")
    if url and url not in urls:
        urls.append(url)

print(f"Found {len(urls)} videos watched today.")

# Visit each video and click the Like button
for url in urls:
    driver.get(url)
    print(f"Navigating to {url}")
    
    try:
        # Target the button directly using the exact DOM structure
        like_xpath = "//like-button-view-model//button"
        like_button = wait.until(EC.presence_of_element_located((By.XPATH, like_xpath)))
        
        # Scroll to the button to ensure it is in the viewport
        driver.execute_script("arguments[0].scrollIntoView(true);", like_button)
        time.sleep(1) 
        
        if like_button.get_attribute("aria-pressed") != "true":
            # Force click via JavaScript to bypass "element intercepted" errors
            driver.execute_script("arguments[0].click();", like_button)
            print(" -> Clicked Like!")
        else:
            print(" -> Already liked.")
            
        time.sleep(2) 
        
    except Exception as e:
        print(f" -> Failed to like: {e}")

# Return to history page when finished
print("Done! Returning to history.")
driver.get("https://www.youtube.com/feed/history")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

# --- 1. Python.org: Extracting Events ---
driver.get("https:www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print("Python Events:", events)

# --- 2. Wikipedia: Clicking Links & Searching ---
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print("Article count:", article_number.text)
article_number.click()

new_link = driver.find_element(By.LINK_TEXT, value="Pages")
new_link.click()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# --- 3. Newsletter: Form filling with ActionChains ---
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

driver.find_element(By.NAME, value="fName").click()

actions = ActionChains(driver)
actions.send_keys("Kacper")
actions.send_keys(Keys.TAB)
actions.send_keys("XYZ")
actions.send_keys(Keys.TAB)
actions.send_keys("Randommail@gmail.com")
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.ENTER)

actions.perform()

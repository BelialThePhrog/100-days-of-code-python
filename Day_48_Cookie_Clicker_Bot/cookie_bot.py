from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = uc.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Allow time for the game to load and accept cookies manually if necessary
time.sleep(20)

big_cookie = driver.find_element(By.ID, value="bigCookie")
start_time = time.time()
timeout_limit = 600

Game_on = True
while Game_on:
    if time.time() - start_time > timeout_limit:
        print("10 minutes have passed.")
        Game_on = False
        break 
        
    for _ in range(100):
        big_cookie.click()
    
    affordable_items = driver.find_elements(By.CSS_SELECTOR, value=".product.enabled")
    
    if affordable_items:
        affordable_items[-1].click()

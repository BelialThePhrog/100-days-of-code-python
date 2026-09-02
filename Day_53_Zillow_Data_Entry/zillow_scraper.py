import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# User Inputs & Search URL Setup
place = input("Enter city/state (e.g. San-Francisco,-CA): ").strip().replace(" ", "-")
min_price = input("Enter minimum price (or press enter to skip): ").strip()
max_price = input("Enter maximum price (or press enter to skip): ").strip()

base_url = f"https://www.zillow.com/homes/for_rent/{place}_rb/"
params = []
if min_price:
    params.append(f"price={min_price}-{max_price if max_price else ''}")
elif max_price:
    params.append(f"price=-{max_price}")
zillow_url = base_url if not params else f"{base_url}?{'&'.join(params)}"

print(f"Fetching listings from: {zillow_url}")

# Selenium setup
options = Options()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
options.add_argument("--lang=en-US")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 15)

all_addresses, all_prices, all_links = [], [], []

try:
    driver.get(zillow_url)

    try:
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a.property-card-link")
        ))
    except Exception:
        print("Listings never loaded — Zillow may be showing a CAPTCHA "
              "or the page structure has changed. Inspect the page manually.")
        driver.quit()
        sys.exit()

    cards = driver.find_elements(By.CSS_SELECTOR, "a.property-card-link")
    seen_links = set()

    for card in cards:
        href = card.get_attribute("href")
        if not href or href in seen_links:
            continue
        seen_links.add(href)

        try:
            address = card.find_element(By.CSS_SELECTOR, "address").text.strip()
        except Exception:
            address = ""
        try:
            price = card.find_element(
                By.XPATH, "./ancestor::div[contains(@class,'property-card')]//*[contains(@class,'price')]"
            ).text.strip()
        except Exception:
            price = ""

        if address and price:
            all_addresses.append(address)
            all_prices.append(price)
            all_links.append(href)

    min_count = len(all_links)
    print(f"Found {min_count} listings ready for entry.")

    if min_count == 0:
        print("No listings scraped — nothing to submit.")
        driver.quit()
        sys.exit()
   
    # Google Form Automation
    FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeTbS7Lx32ivbv97u3y-cB9Nph1F9k31jgUoYGGwfFf7YKs9A/viewform?usp=header"
    submitted = 0

    for i in range(min_count):
        driver.get(FORM_URL)
        inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "input.whsOnd, textarea.KHxj8b")
            )
        )

        if len(inputs) < 3:
            print(f"Skipping entry {i}: form only exposed {len(inputs)} field(s), expected 3.")
            continue

        inputs[0].send_keys(all_addresses[i])
        inputs[1].send_keys(all_prices[i])
        inputs[2].send_keys(all_links[i])

        try:
            submit_btn = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//span[contains(text(),'Submit') or contains(text(),'Wysyłaj') "
                "or contains(text(),'Prześlij')]/ancestor::div[@role='button']",
            )))
            submit_btn.click()
            submitted += 1
            time.sleep(1)
        except Exception as e:
            print(f"Failed to submit entry {i} ({all_addresses[i]}): {e}")

    print(f"Done. Submitted {submitted}/{min_count} entries successfully.")

finally:
    driver.quit()

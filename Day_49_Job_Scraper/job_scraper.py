import time
import urllib.parse
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def build_search_url(keyword: str, location: str) -> str:
    """
    Pracuj.pl encodes search results directly in the URL:
        https://www.pracuj.pl/praca/{keyword};kw/{location};wp
    Going straight to this URL is much more reliable than filling in the
    homepage search form, since it skips the cookie banner blocking the
    inputs and any changes to the form's field selectors.
    """
    kw = urllib.parse.quote(keyword.strip())
    loc = urllib.parse.quote(location.strip())
    if loc:
        return f"https://www.pracuj.pl/praca/{kw};kw/{loc};wp"
    return f"https://www.pracuj.pl/praca/{kw};kw"

def dismiss_cookie_banner(driver, wait):
    """
    Best-effort click on the cookie-consent button. Wrapped so that if the
    banner text/selector changes (or it doesn't appear at all), the script
    keeps going instead of crashing.
    """
    candidates = [
        (By.XPATH, "//button[contains(., 'Akceptuj wszystkie')]"),
        (By.XPATH, "//button[contains(., 'Zaakceptuj')]"),
        (By.XPATH, "//button[contains(., 'Zgadzam się')]"),
        (By.ID, "onetrust-accept-btn-handler"),
    ]
    for by, sel in candidates:
        try:
            btn = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((by, sel)))
            btn.click()
            print("Cookie banner dismissed.")
            return
        except Exception:
            continue
    print("No cookie banner found (or already dismissed) — continuing.")

def main():
    job_title = input("Enter job title or category (e.g., Python Developer): ")
    location = input("Enter location (e.g., Warszawa): ")

    chrome_options = uc.ChromeOptions()
    driver = uc.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 15)

    try:
        url = build_search_url(job_title, location)
        print(f"Opening: {url}")
        driver.get(url)

        dismiss_cookie_banner(driver, wait)

        # Wait for job offer listings to actually render before continuing.
        # data-test="section-offers" wraps the results list on pracuj.pl.
        try:
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[data-test="section-offers"], [data-test="list-offer"]')
                )
            )
            print("Results loaded.")
        except Exception:
            print("Results container not detected within timeout — page may "
                  "still have loaded results under a different layout, check manually.")

    except Exception as e:
        print(f"An error occurred during automation: {e}")
    finally:
        input("\nPress Enter to close the browser and terminate the script...")
        driver.quit()

if __name__ == "__main__":
    main()

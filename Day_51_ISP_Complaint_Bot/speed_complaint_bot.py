import os
import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuration 
PROMISED_DOWN = 150.0  # Replace with your plan's download speed
PROMISED_UP = 50.0     # Replace with your plan's upload speed
MY_EMAIL = "example_of_an_email@gmail.com"
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")  
TO_EMAIL = "your_internet_provider@gmail.com"

# Selenium Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net/")
time.sleep(10) 

go_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='start speed test - connection type multi']")
go_button.click()

time.sleep(60) 

result_url = driver.current_url
speed_elements = driver.find_elements(By.CSS_SELECTOR, ".py-2.font-mono.text-5xl.MuiBox-root.css-s31qlv")
download_speed = speed_elements[0].text
upload_speed = speed_elements[1].text

# Logic & Email Trigger
# Convert extracted text to floats for mathematical comparison
down = float(download_speed)
up = float(upload_speed)

print(f"Result URL: {result_url}")
print(f"Download: {down} Mbps")
print(f"Upload: {up} Mbps")

if down < PROMISED_DOWN or up < PROMISED_UP:
    print("Speeds are below threshold. Sending email...")
    
    # Email composition
    email_body = (
        f"Subject: Internet Speed Inquiry - Account [Your Account Number]\n\n"
        f"Dear Customer Service,\n\n"
        f"I hope this email finds you well.\n\n"
        f"I am reaching out because my current internet speeds are lower than expected "
        f"based on my plan's guaranteed speeds of {PROMISED_DOWN} Mbps down and {PROMISED_UP} Mbps up.\n\n"
        f"I just ran a diagnostic test, and my latest results are:\n"
        f"Download: {down} Mbps\n"
        f"Upload: {up} Mbps\n"
        f"Test result link: {result_url}\n\n"
        f"Could you please look into my connection and let me know if there are any outages or issues on my line?\n\n"
        f"Thank you,\n"
        f"[Your Name]"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=email_body
        )
    print("Email successfully sent.")
else:
    print("Speeds are acceptable. No email sent.")

driver.quit()

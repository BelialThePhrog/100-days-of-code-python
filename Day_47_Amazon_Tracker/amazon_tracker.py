import requests
import string
import smtplib
from bs4 import BeautifulSoup

my_email = "YOUR_EMAIL@gmail.com"
password = "YOUR_APP_PASSWORD"
recipient_email = "addreser@gmail.com"

max_price = float(input("Enter max price: "))

# Headers to bypass basic bot-detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
}

try:
    url = "https://www.amazon.com/Quantum-Computation-Information-10th-Anniversary/dp/1107002176/ref=sr_1_2?crid=1CLLFWZ2BTK71&dib=eyJ2IjoiMSJ9.6MC5ADpJx0ZP-1h4q8nw3gHgMa8af4HD-YbwVTNmcOuHHhgsxUAOomxst9ek_V4Qxhnmz_QbKgYMWqH_t1EtO4XDTGgBQIMG24-9gGOXjHPrmOpcbgHDjt4O6c3svsOIfmPa1rWbVh_JOajvjIaj5B6NnyGp4CeKVjUnNMHVaEwTkLEyHz0Dln5QlHIjPDizwWWJL6ue3GKdLS4FOOx0FeDmBBVhOL3PzidGGe_cQeM.iyAnnnulRmGw2d-dpAz3M-NaLZGoqcs4Pmz4U8NY2zE&dib_tag=se&keywords=quantum+computing&qid=1787809099&s=books&sprefix=quantum+computinh%2Cstripbooks-intl-ship%2C220&sr=1-2"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_span = soup.find(id="apex-pricetopay-accessibility-label")
    
    if price_span:
        raw_text = price_span.text.strip()
        print(f"Found Text: '{raw_text}'")
      
        no_digits = string.printable[10:]
        trans = str.maketrans(no_digits, " "*len(no_digits))
        translated_text = raw_text.translate(trans)
        
        first_number_str = translated_text.split()[0]
        second_number_str = translated_text.split()[1]
        actual_price = float(f"{first_number_str}.{second_number_str}")
        
        if actual_price < max_price:      
            print(f"BINGO! Prize: {actual_price}")
            print("Sending email alert...")
            
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                msg_body = f"Subject: Amazon Price Drop Alert!\n\nThe item is under your max price! Current price: {actual_price}"
                connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=msg_body)
                
            print("Email sent successfully.")
        else:
            print(f"Found element, but the price ({actual_price}) is higher than your max price ({max_price}).")
    else:
        print("Did not find ID 'apex-pricetopay-accessibility-label'.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

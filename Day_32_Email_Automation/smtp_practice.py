# ==========================================
#SMTP CONNECTION PRACTICE
# ==========================================
# Note: Replace placeholders with valid credentials. 
# Do not use your primary account password; use a generated 'App Password'.

my_email = "example_of_an_email@gmail.com"
password = "YOUR_APP_PASSWORD_HERE" # DO NOT commit real passwords!

try:
    connection = smtplib.SMTP("smtp.gmail.com")
    
    connection.starttls()
  
    connection.login(user=my_email, password=password)
    
    
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="addreser@gmail.com", 
        msg="Subject:Hello\n\nThis is a test email sent from Python."
    )
    print("Email successfully sent.")
except Exception as e:
    print(f"Connection or authentication failed: {e}")
finally:
  
    connection.close()

# ==========================================
# DATETIME & CONDITIONAL AUTOMATION
# ==========================================
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday() # Monday is 0, Tuesday is 1, etc.

print(f"Current Year: {year}")
print(f"Current Day Index: {day_of_week}")

# Execute a routine only if today is Tuesday (index 1)
if day_of_week == 1:
    print("It's Tuesday! Triggering the automated email sequence...")
    # (The SMTP connection code would typically go here

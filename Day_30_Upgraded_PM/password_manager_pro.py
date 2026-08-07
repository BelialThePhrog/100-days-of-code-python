import tkinter as tk
from tkinter import messagebox
import random as r
import json

FONT_NAME = "Courier"

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "\\", "|",
    ";", ":", "'", '"', ",", ".",
    "<", ">", "/", "?", "`", "~"
]
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def pass_search():
    website = website_entry.get()
    
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search.")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message=f"No details for {website} exist.")
        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    # Clear the entry box first so passwords don't stack if clicked twice
    password_entry.delete(0, "end")
    
    password = ""
    for letter in range(0,20):
        l = r.randint(0,51)
        password += letters[l]
    for number in range(0,5):
        n = r.randint(0,9)
        password += numbers[n]
    for symbol in range(0,5):
        s = r.randint(0,31)
        password += symbols[s]
        
    new_password = list(password)
    r.shuffle(new_password)
    new_final_password = "".join(new_password)
    
    password_entry.insert(0, new_final_password)
    window.clipboard_clear()
    window.clipboard_append(new_final_password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    value_1 = website_entry.get()
    value_2 = email_entry.get()
    value_3 = password_entry.get()
    
    # new_data MUST be inside the function so it captures the current entry values
    new_data = {
        value_1: {
            "email": value_2,
            "password": value_3
        }
    }
    
    # Check if fields are empty
    if len(value_1) == 0 or len(value_3) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            # Try to read the old data
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            # If file doesn't exist, create it and dump new_data
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # If file exists, update old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Save the updated data
                json.dump(data, file, indent=4)
        finally:
            messagebox.showinfo("Saved!", "Your password has been saved!")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            # We usually don't delete the email as users reuse the same email

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# --- LOGO (Row 0) ---
canvas = tk.Canvas(height=200, width=200)
# Make sure "logo.png" is in the exact same folder as this script
try:
    logo_img = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
except tk.TclError:
    print("Logo image not found. Ensure 'logo.png' is in the directory.")
canvas.grid(row=0, column=1)

# --- LABELS (Column 0) ---
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

# --- ENTRIES & BUTTONS ---

# Website Entry: Spans across Column 1 and Column 2
website_entry = tk.Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus() 

# Email Entry: Spans across Column 1 and Column 2
email_entry = tk.Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "your_email@gmail.com") 

# Password Entry: Sits only in Column 1
password_entry = tk.Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Generate Password Button: Sits only in Column 2
generate_password_button = tk.Button(text="Generate Password", command=pass_generate)
generate_password_button.grid(row=3, column=2, sticky="EW")
# Generate Search Button: Sits only in Column 2
generate_search_button = tk.Button(text="Search", command=pass_search)
generate_search_button.grid(row=1, column=2, sticky="EW")

# Add Button: Spans across Column 1 and Column 2
add_button = tk.Button(text="Add", command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()

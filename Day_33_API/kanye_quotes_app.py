from tkinter import *
import requests

def get_quote():
    try:
        response = requests.get(url="https://api.kanye.rest")
        response.raise_for_status()
        quote = response.json()["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException as e:
        canvas.itemconfig(quote_text, text="Error fetching data.")
        print(f"API Error: {e}")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
try:
    background_img = PhotoImage(file="background.png")
    kanye_img = PhotoImage(file="kanye.png")
    
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Click Kanye for a quote", width=250, font=("Arial", 30, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)
except TclError:
    print("Images not found. Ensure 'background.png' and 'kanye.png' are in the directory.")

window.mainloop()

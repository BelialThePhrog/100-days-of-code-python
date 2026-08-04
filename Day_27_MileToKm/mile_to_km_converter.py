import tkinter

def button_clicked():
    """
    Fetches the value from the entry box, converts miles to kilometers,
    and updates the result label.
    """
    try:
        miles = float(box.get())
        km = round(miles * 1.60934, 2)
        my_label_4.config(text=f"{km}")
    except ValueError:
        my_label_4.config(text="Error")

# Window setup
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Entry Box
box = tkinter.Entry(width=10)
box.grid(column=1, row=0)

# Labels
my_label_1 = tkinter.Label(text="Miles")
my_label_1.grid(column=2, row=0)

my_label_2 = tkinter.Label(text="is equal to")
my_label_2.grid(column=0, row=1)

my_label_4 = tkinter.Label(text="0")
my_label_4.grid(column=1, row=1)

my_label_3 = tkinter.Label(text="Km")
my_label_3.grid(column=2, row=1)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Keep window open
window.mainloop()

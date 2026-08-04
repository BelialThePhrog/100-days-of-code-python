import tkinter

def button_clicked():
    """
    Update the label text with the content typed into the entry box.
    """
    print("Button got clicked!")
    my_label.config(text=input_1.get())

# 1. Window Initialization
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# 2. Label
my_label = tkinter.Label(text="I am a label")
my_label.grid(column=1, row=1)

# Modify label text (two different ways)
my_label["text"] = "new text"
my_label.config(text="next text")

# 3. Buttons
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

button_2 = tkinter.Button(text="Don't Click me", command=button_clicked)
button_2.grid(column=3, row=1)

# 4. Entry (Input Box)
input_1 = tkinter.Entry()
input_1.grid(column=4, row=4)

# Keep window running
window.mainloop()

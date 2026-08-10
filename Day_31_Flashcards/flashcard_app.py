import tkinter as tk
import random as r
import pandas as pd
import time
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

# ==========================================
# DATA SETUP & STREAK TRACKING
# ==========================================
try:
    list_to_learn = pd.read_csv("french_words.csv")
    to_learn_dict = list_to_learn.to_dict(orient="records")
except FileNotFoundError:
    # If the file doesn't exist, create a dummy fallback
    to_learn_dict = [{"French": "Error", "English": "Error"}]

try:
    # Try to load the known words file if it exists
    known_words_data = pd.read_csv("known_words.csv")
    known_words_dict = known_words_data.to_dict(orient="records")
except FileNotFoundError:
    # If it's the user's first time, this file won't exist yet, so we start with an empty list
    known_words_dict = []

# This dictionary will track how many times in a row a specific French word was passed.
# It will look like this behind the scenes: {"bonjour": 3, "oui": 1}
streak_tracker = {}
current_card = {}
correct = 0
wrong = 0

# -------------- Functionality --------------
def flipping():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    chance = r.randint(1, 100)
    
    # If chance is 1-95 (95% chance) OR if the user has no known words yet...
    if chance <= 95 or len(known_words_dict) == 0:
        # We must also make sure there are actually words left to learn!
        if len(to_learn_dict) > 0:
            current_card = r.choice(to_learn_dict)
        else:
            # Fallback if they learned every single word
            current_card = r.choice(known_words_dict)
            
    # If chance is 96-100 (5% chance) and they have known words to review...
    else:
        current_card = r.choice(known_words_dict)
    
    # Update Flashcard UI
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    
    # Update Score UI
    canvas.itemconfig(score_text, text=f"Correct: {correct} | Wrong: {wrong}")
    
    flip_timer = window.after(2000, func=flipping)

# ==========================================
# PASS / FAIL & FILE MOVEMENT LOGIC
# ==========================================
def Passed():
    global correct, streak_tracker, to_learn_dict, known_words_dict
    correct += 1
    
    word = current_card["French"]
    
    if word not in streak_tracker:
        streak_tracker[word] = 1
    else:
        streak_tracker[word] += 1
        
    if streak_tracker[word] == 5:
        should_move = messagebox.askyesno(
            title="Word Mastered!", 
            message=f"You got '{word}' correct 5 times in a row!\n\nDo you want to move it to your known words list?"
        )
        
        # If they click "Yes" AND the word is still in the to_learn_dict
        if should_move and current_card in to_learn_dict:
            # 1. Remove it from the learning list
            to_learn_dict.remove(current_card)
            
            # 2. Add it to the known words list
            known_words_dict.append(current_card)
            
            # 3. Save the updated learning list to the original CSV
            # We convert the list of dicts back to a DataFrame to save it easily
            pd.DataFrame(to_learn_dict).to_csv("french_words.csv", index=False)
            
            # 4. Save the updated known words list to a new CSV
            pd.DataFrame(known_words_dict).to_csv("known_words.csv", index=False)
            
            # 5. Optional: Remove the word from the streak tracker to clear memory
            del streak_tracker[word]
            
    # Finally, pull a new word
    new_word()

def Failed():
    global wrong, streak_tracker
    wrong += 1
    
    word = current_card["French"]
    
    # If they get it wrong, we harshly reset their streak back to 0!
    streak_tracker[word] = 0
    
    # Pull a new word
    new_word()
    
# -------------- UI --------------
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flipping)

# --- CANVAS ---
canvas = tk.Canvas(height=650, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)

try:
    card_front_img = tk.PhotoImage(file="card_front.png")
    card_back_img = tk.PhotoImage(file="card_back.png")
    # Store the image as an item so we can change it later for the flashcard flip!
    canvas_image = canvas.create_image(400, 300, image=card_front_img)
except tk.TclError:
    print("Card image not found. Ensure 'card_front.png' and 'card_back.png' are in the directory.")
    
card_title = canvas.create_text(400, 200, text="", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", fill="black", font=("Arial", 60, "bold"))
score_text = canvas.create_text(400, 100, text=f"Correct: {correct} | Wrong: {wrong}", fill="black", font=("Arial", 20, "italic"))

canvas.grid(row=1, column=1)

# --- BUTTONS ---
try:
    imagetest_0 = tk.PhotoImage(master=window, file="right.png")
    imagetest_1 = tk.PhotoImage(master=window, file="wrong.png")
except tk.TclError:
    print("Button images not found. Ensure 'right.png' and 'wrong.png' are in the directory.")

Pass_button = tk.Button(window, image=imagetest_0, borderwidth=0, relief="flat", command=Passed)
Fail_button = tk.Button(window, image=imagetest_1, borderwidth=0, relief="flat", command=Failed)

Pass_button.place(x=150, y=575)
Fail_button.place(x=550, y=575)

new_word()

window.mainloop()

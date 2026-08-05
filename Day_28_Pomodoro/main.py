import tkinter
from tkinter import messagebox
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
times = {"work": 0, "short": 0, "long": 0, "confirmed": False}

# ---------------------------- DYNAMIC TIME SETUP ------------------------------- #
def ask_for_time():
    dialog = tkinter.Toplevel(window)
    dialog.title("Timer Settings")
    dialog.config(padx=20, pady=20, bg=YELLOW)
    
    local_times = {"work": 0, "short": 0, "long": 0, "confirmed": False}
    
    def use_default():
        local_times["work"] = 25
        local_times["short"] = 5
        local_times["long"] = 20
        local_times["confirmed"] = True
        dialog.destroy()
        
    def submit():
        hours = int(hours_spinbox.get())
        minutes = int(minutes_spinbox.get())
        loops = int(loops_spinbox.get())
        
        total_time = (hours * 60) + minutes
        
        if total_time <= 0:
            messagebox.showerror("Error", "Time must be greater than 0!")
            return
            
        unit = total_time / (loops * 27)
        
        work_min = round(unit * 5)
        short_break_min = round(unit * 1)
        long_break_min = round(unit * 4)
        
        if work_min < 20:
            suggested_loops = math.floor(total_time / 108)
            if suggested_loops < 1:
                suggested_loops = 1
                
            warning_msg = (f"Bad idea! Work time is only {work_min} min.\n"
                           f"We suggest decreasing the number of loops to {suggested_loops}, "
                           f"so the work time is at least 20 minutes.\n\n"
                           f"Do you want to adjust your settings?")
            
            if messagebox.askyesno("Warning", warning_msg):
                return
                
        confirm_msg = (f"Calculated times:\n"
                       f"Work: {work_min} min\n"
                       f"Short break: {short_break_min} min\n"
                       f"Long break: {long_break_min} min\n\n"
                       f"Do you confirm these values?")
                       
        if messagebox.askyesno("Confirmation", confirm_msg):
            local_times["work"] = work_min
            local_times["short"] = short_break_min
            local_times["long"] = long_break_min
            local_times["confirmed"] = True
            dialog.destroy()

    tkinter.Label(dialog, text="Hours:", bg=YELLOW).grid(row=0, column=0, pady=5)
    hours_spinbox = tkinter.Spinbox(dialog, from_=0, to=12, width=5)
    hours_spinbox.grid(row=0, column=1)
    
    tkinter.Label(dialog, text="Minutes:", bg=YELLOW).grid(row=1, column=0, pady=5)
    minutes_spinbox = tkinter.Spinbox(dialog, from_=0, to=59, width=5)
    minutes_spinbox.grid(row=1, column=1)
    
    tkinter.Label(dialog, text="Loops:", bg=YELLOW).grid(row=2, column=0, pady=5)
    loops_spinbox = tkinter.Spinbox(dialog, from_=1, to=20, width=5)
    loops_spinbox.grid(row=2, column=1)
    
    submit_button = tkinter.Button(dialog, text="Calculate & Confirm", command=submit)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    default_button = tkinter.Button(dialog, text="Default (25/5/20)", command=use_default)
    default_button.grid(row=4, column=0, columnspan=2, pady=5)
    
    window.wait_window(dialog)
    
    return local_times

# ---------------------------- TIMER RESET ------------------------------- # 
def button_clicked():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global times
    
    reps += 1
    if reps == 1:
        times = ask_for_time()
    
    if times["confirmed"] and reps != 8 and reps % 2 == 1:
        title_label.config(text="WORK", fg=RED)
        timer.grid(column=2, row=1)
        countdown(times["work"] * 60)
    elif times["confirmed"] and reps != 8 and reps % 2 == 0:
        title_label.config(text="SHORT BREAK", fg=GREEN)
        timer.grid(column=2, row=1)
        countdown(times["short"] * 60)
    elif times["confirmed"] and reps == 8:
        title_label.config(text="LONG BREAK", fg=PINK)
        timer.grid(column=2, row=1)
        countdown(times["long"] * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count == 9:
        window.lift()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        reps_completed = math.floor(reps/2)
        checkmarks.config(text=reps_completed*"✔")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

title_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
title_label.grid(column=2, row=1)

button_start = tkinter.Button(text="Start", command=start_timer)
button_stop = tkinter.Button(text="Stop", command=button_clicked)

button_start.grid(column=1, row=3)
button_stop.grid(column=3, row=3)

checkmarks = tkinter.Label(bg=YELLOW, fg=GREEN)
checkmarks.grid(column=2, row=4)
                  
window.mainloop()

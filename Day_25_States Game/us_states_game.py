import turtle
import pandas as pd

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --- Load Data ---
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# --- Setup Timer ---
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(-150, 200)

# Global timer variable (in seconds)
time_left = 600  

def update_timer():
    global time_left
    timer_turtle.clear()
    
    if time_left > 0:
        timer_turtle.write(f"Time: {time_left}s", align="center", font=("Arial", 20, "bold"))
        time_left -= 1
        screen.ontimer(update_timer, 1000)
    else:
        timer_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))

def play_game():
    # Stop the game if time is up or player wins
    if time_left <= 0 or len(guessed_states) >= 50:
        return

    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", 
        prompt="What's another state's name?"
    )
    
    if answer_state:
        answer_state = answer_state.title()
        
        # Check if it's a valid state and hasn't been guessed yet
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            
            # Fetch coordinates
            state_data = data[data.state == answer_state]
            x_cord = int(state_data.x.iloc[0])
            y_cord = int(state_data.y.iloc[0])
            
            # Write state name on map
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            writer.color("black")
            writer.goto(x_cord, y_cord)
            writer.write(answer_state, align="center", font=("Arial", 10, "normal"))
            
    # Continue the game loop
    if len(guessed_states) < 50 and time_left > 0:
        screen.ontimer(play_game, 100)

# --- Start Game Execution ---
update_timer()
screen.ontimer(play_game, 500)

screen.mainloop()

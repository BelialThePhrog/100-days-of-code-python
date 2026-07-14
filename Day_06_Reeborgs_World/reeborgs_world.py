# Day 6 Project - Reeborg's World
# Note: This code is designed to run in the Reeborg's World environment.
# It uses environment-specific built-in functions (move, turn_left, at_goal, etc.).

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Solving the challenge using a while loop
while not at_goal():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

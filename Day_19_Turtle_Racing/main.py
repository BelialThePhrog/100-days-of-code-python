import turtle as tur
import random as r

# Screen setup
screen = tur.Screen()
screen.setup(width=500, height=400)

# Get user input via GUI dialogs
turtle_number = int(screen.numinput(
    title="Participants", 
    prompt="How many turtles are taking part in a race? (2 to 10)", 
    minval=2, 
    maxval=10
))

colors = ["green", "brown", "yellow", "red", "orange", "black", "olive", "pink", "grey", "white"]
colors_taking_part = colors[:turtle_number]

bet = screen.textinput(
    title="Make your bet", 
    prompt=f"Place your bet. Which color will win?\n{colors_taking_part}"
)

my_turtles = []

# Instantiate and position turtles
for i in range(turtle_number):
    new_turtle = tur.Turtle(shape="turtle")
    new_turtle.color(colors_taking_part[i])
    new_turtle.penup()
    # Aligning at the start line
    new_turtle.goto(-150, -150)
    new_turtle.left(90)
    new_turtle.forward(30 * i)
    new_turtle.right(90)
    my_turtles.append(new_turtle)

finished = False

# Main race loop
while not finished:
    # Pick a random turtle from the list
    random_turtle = r.choice(my_turtles)
    random_move = r.randint(5, 10)
    random_turtle.forward(random_move)
    
    # Check if the turtle crossed the finish line
    if random_turtle.xcor() > 150:
        finished = True
        winning_color = random_turtle.pencolor()
        
        # Display the result
        writer = tur.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(0, 0)
        
        if winning_color == bet:
            message = f"You won the bet! The {winning_color} turtle won."
        else:
            message = f"You lost the bet. The {winning_color} turtle won."
            
        writer.write(message, align="center", font=("Arial", 16, "bold"))

screen.exitonclick()

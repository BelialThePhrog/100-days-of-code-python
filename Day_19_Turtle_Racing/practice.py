import turtle as tur

tim = tur.Turtle()
screen = tur.Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(45)
    
def turn_right():
    tim.right(45)
    
def reset():
    tim.reset()

# Event listeners
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="r", fun=reset)

screen.exitonclick()

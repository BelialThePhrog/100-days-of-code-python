import turtle as tur
import time
from snake import Snake

# Screen setup
screen = tur.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

# Initialize Snake
snake = Snake()

# Event listeners for controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
screen.exitonclick()

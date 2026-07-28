import turtle as tur
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = tur.Screen()
screen.setup(width=1200, height=1000)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create the player paddle on the left
player_paddle = Paddle((-550, 0))

# Create the computer paddle on the right 
computer_paddle = Paddle((550, 0))

ball = Ball()
scoreboard = Scoreboard()

movement = 1

screen.listen()
screen.onkey(player_paddle.go_up, "Up")
screen.onkey(player_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    computer_direction = "up"

    # Computer Paddle AI Logic
    if movement == 0:
        computer_direction = "down"
        if computer_paddle.paddle.ycor() < -450:
            movement = 1
    elif movement == 1:
        computer_direction = "up"
        if computer_paddle.paddle.ycor() > 450:
            movement = 0
        
    if computer_direction == "up":
        computer_paddle.go_up()
    else:
        computer_paddle.go_down()
    
    # Collision with Player Paddle
    if player_paddle.paddle.distance(ball.ball) < 100 and ball.ball.xcor() < -520:
        ball.change_direction()
        
    # Collision with Computer Paddle
    if computer_paddle.paddle.distance(ball.ball) < 50 and ball.ball.xcor() < 580:
        ball.change_direction()

    # Out of bounds (Player misses)
    if ball.ball.xcor() < -580:
        ball.reset_ball()
        scoreboard.increase_score_computer()
        
    # Out of bounds (Computer misses)
    if ball.ball.xcor() > 580:
        ball.reset_ball()
        scoreboard.increase_score_player()
        
    # Win Condition
    if scoreboard.points_1 > 10 or scoreboard.points_2 > 10:
        game_is_on = False
        scoreboard.game_over()
        
screen.exitonclick()

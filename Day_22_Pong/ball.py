import turtle as tur

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Ball:
    def __init__(self):
        self.ball = tur.Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=1, stretch_len=1) 
        self.ball.penup()
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_y = self.ball.ycor() + self.move_y
        new_x = self.ball.xcor() + self.move_x
        self.ball.goto(new_x, new_y)
        
        # Wall collision logic
        if self.ball.ycor() > 480 or self.ball.ycor() < -480:
            self.move_y *= -1

    def change_direction(self):
        self.move_x *= -1

    def reset_ball(self):
        self.ball.goto(0, 0)
        self.move_x *= -1

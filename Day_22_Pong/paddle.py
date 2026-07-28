import turtle as tur

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:
    def __init__(self, position):
        self.paddle = tur.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1) 
        self.paddle.penup()
        self.paddle.goto(position)
    
    def go_up(self):
        if self.paddle.ycor() < 500:
            new_y = self.paddle.ycor() + 20
            self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        if self.paddle.ycor() > -450:
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(self.paddle.xcor(), new_y)

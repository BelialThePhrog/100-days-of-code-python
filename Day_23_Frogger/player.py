import turtle as tur

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player:
    def __init__(self):
        self.player_turtle = tur.Turtle()
        self.player_turtle.shape("turtle")
        self.player_turtle.color("white")
        self.player_turtle.penup()
        self.player_turtle.teleport(x=0, y=-280)
        self.player_turtle.setheading(UP)

    def move(self):
        self.player_turtle.forward(MOVE_DISTANCE)
    
    def left(self):
        if self.player_turtle.xcor() > -600:
            self.player_turtle.setheading(LEFT) 
            self.player_turtle.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.player_turtle.ycor() < 350:
            self.player_turtle.setheading(UP)
            self.player_turtle.forward(MOVE_DISTANCE)

    def right(self):
        if self.player_turtle.xcor() < 600:
            self.player_turtle.setheading(RIGHT)
            self.player_turtle.forward(MOVE_DISTANCE)

    def down(self):
        if self.player_turtle.ycor() > -290:
            self.player_turtle.setheading(DOWN)
            self.player_turtle.forward(MOVE_DISTANCE)

    def reset_position(self): 
        self.player_turtle.goto(0, -280)

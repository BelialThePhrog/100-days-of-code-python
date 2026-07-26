import turtle as tur

# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            new_turtle = tur.Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.teleport(x=-20*i, y=0)
            self.segments.append(new_turtle)
            
    def move(self):
        # Move each segment to the position of the previous segment
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg-1].pos())
        
        # Move the head forward
        self.segments[0].forward(MOVE_DISTANCE)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

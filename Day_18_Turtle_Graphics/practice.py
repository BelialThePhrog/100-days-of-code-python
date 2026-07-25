import turtle
import random as r
from turtle import Screen


tom = turtle.Turtle()
tom.shape("turtle")
turtle.colormode(255)

# -----------------------------------------------------------
# Uncomment selected block
# -----------------------------------------------------------

# # Challenge 1 - Drawing a square
# tom.color("red")
# for i in range(4):
#     tom.forward(100)
#     tom.left(90)

# # Challenge 2 - Drawing a dashed line
# tom.color("red")
# for i in range(4):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()

# # Challenge 3 - Drawing Shapes (Triangle to Decagon)
# for i in range(2, 11):
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     tom.pencolor((red, green, blue))
#     for x in range(i):
#         tom.forward(100)
#         tom.left(360 / i)

# # Challenge 4 - Drawing a Random Walk
# tom.pensize(10)
# tom.speed("fast")
# for i in range(120):
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     choice = r.randint(1, 4)
#     tom.pencolor((red, green, blue))
#     tom.forward(30)
#     tom.left(choice * 90)

# # Challenge 5 - Drawing a Spirograph
# tom.speed(0)
# for i in range(120):
#     red = r.randint(0, 255)
#     green = r.randint(0, 255)
#     blue = r.randint(0, 255)
#     tom.color((red, green, blue))
#     tom.circle(100)
#     tom.left(360 / 120)

# -----------------------------------------------------------
screen = Screen()
screen.exitonclick()

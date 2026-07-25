import turtle
import random as r
from turtle import Screen
import colorgram

# Extract colors from the image
many_colors = int(input("How many colors you want to extract? "))
colors = colorgram.extract('sweet_pic.png', many_colors)

# Turtle setup
tom = turtle.Turtle()
tom.shape("turtle")
tom.speed(0)
turtle.colormode(255)
turtle.bgcolor("black")

# Screen setup
screen = Screen()
width = screen.window_width()
height = screen.window_height()
screen.setworldcoordinates(-1, -1, width, height)

# Drawing logic
total_dots = int(round(width * height / 100, 0))

for i in range(1, total_dots):
    # Select random color from extracted palette
    x = r.randint(0, many_colors - 1)
    first_color = colors[x]
    red = first_color.rgb[0]
    green = first_color.rgb[1]
    blue = first_color.rgb[2]
    tup = (red, green, blue)
    
    # Draw dot
    tom.dot(10, tup)
    tom.penup()
    tom.forward(width / 10)
    
    # Grid turning logic
    if i % 20 == 0:
        tom.left(270)
        tom.dot(10, tup)
        tom.forward(height / 10)
        tom.left(270)
    elif i % 10 == 0:
        tom.left(90)
        tom.dot(10, tup)
        tom.forward(height / 10)
        tom.left(90)

screen.exitonclick()

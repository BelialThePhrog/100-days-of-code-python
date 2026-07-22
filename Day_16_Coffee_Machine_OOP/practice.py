# Object-Oriented Programming Basics (Turtle Graphics)

import turtle as t

timmy = t.Turtle()
t.color("orchid")
print(timmy)
t.forward(100)

my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Installing External Packages
# Note: During the learning process in Jupyter Notebook, 
# third-party packages were installed using pip commands, such as:
# %pip install lb-pretty-table

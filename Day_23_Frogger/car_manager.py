import turtle as tur
import random as r

class CarManager:
    def __init__(self, car_speed):
        self.car = tur.Turtle()
        self.car.shape("square")
        
        red = r.randint(0, 255)
        green = r.randint(0, 255)
        blue = r.randint(0, 255)
        
        y_cor = r.randint(-250, 250)
        x_cor = r.choice([1, -1])
        
        self.car.color(red, green, blue)
        self.car.penup()
        self.car.teleport(x = 600 * x_cor, y = y_cor)
        self.car.shapesize(stretch_wid=0.5, stretch_len=3)
        
        if x_cor == 1:
            self.move_x = -car_speed
        else:
            self.move_x = car_speed
            
        self.car.speed(car_speed)

    def move(self):
        new_y = self.car.ycor()
        new_x = self.car.xcor() + self.move_x
        self.car.goto(new_x, new_y)
        
        if self.car.xcor() > 650 or self.car.xcor() < -650:
            self.car.hideturtle()

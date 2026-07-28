import turtle as tur
import random as r

class Scoreboard(tur.Turtle): 
    def __init__(self):
        super().__init__()
        self.points_1 = 0
        self.points_2 = 0
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=0.3) 
        self.color("white")
        self.speed("fastest")
        self.teleport(0, 450)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.points_1} : {self.points_2} ", False, align="center", font=("Arial", 20, "bold"))

    def increase_score_player(self):
        self.points_1 += 1
        self.update_scoreboard() 
        
    def increase_score_computer(self):
        self.points_2 += 1
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 30, "bold"))

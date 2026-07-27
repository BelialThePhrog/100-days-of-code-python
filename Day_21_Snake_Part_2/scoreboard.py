import turtle as tur

class Scoreboard(tur.Turtle): 
    
    def __init__(self):
        super().__init__()
        self.points = 0
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=0.3) 
        self.color("white")
        self.speed("fastest")
        self.teleport(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.points}", False, align="center", font = ("Arial", 12, "bold"))

    def increase_score(self):
        self.points += 1
        self.update_scoreboard() 

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", False, align="center", font = ("Arial", 30, "bold"))

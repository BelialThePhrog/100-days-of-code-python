import turtle as tur

class Scoreboard(tur.Turtle): 
    def __init__(self):
        super().__init__()
        self.points_1 = 0
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=0.3) 
        self.color("white")
        self.speed("fastest")
        self.teleport(-550, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points_1}", False, align="left", font=("Arial", 18, "bold"))

    def increase_score_player(self):
        self.points_1 += 1
        self.update_scoreboard() 
        
    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 30, "bold"))

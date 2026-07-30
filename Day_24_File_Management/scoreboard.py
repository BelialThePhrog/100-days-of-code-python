import turtle as tur

class Scoreboard(tur.Turtle): 
    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
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
        self.write(f"Score: {self.points}  High Score: {self.highscore}", False, align="center", font=("Arial", 12, "bold"))

    def increase_score(self):
        self.points += 1
        self.update_scoreboard() 

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.points = 0
        self.update_scoreboard()

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#72FF13")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 690)
        self.scoreboard = self.write(f"Score: {self.score}", align="center", font=('Arial', 15, 'bold'))

    
    def add_score(self):
        self.score += 1
        self.clear()
        self.scoreboard = self.write(f"Score: {self.score}", align="center", font=('Arial', 15, 'bold'))
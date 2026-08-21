from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 170)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)

    def calculate_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
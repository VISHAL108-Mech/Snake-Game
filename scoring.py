"""Scoring for Snake Game"""

from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    """Score class for Snake Game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("black")
        self.penup()
        self.goto(0, 170)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score"""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            ALIGN,
            FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Display game over message"""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGN, FONT)

    def calculate_score(self):
        """Calculate and update the score"""
        self.score += 1
        self.update_scoreboard()

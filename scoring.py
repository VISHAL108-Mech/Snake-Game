"""Scoring for Snake Game"""

from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    """Score class for Snake Game"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 170)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score"""
        self.write(f"Score: {self.score}", False, ALIGN, FONT)

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGN, FONT)

    def calculate_score(self):
        """Calculate and update the score"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

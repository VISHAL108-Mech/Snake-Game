from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("blue")
        self.speed(0)


    def generate_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-180, 180)
        self.goto(rand_x, rand_y)
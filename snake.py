"""Snake module for Snake Game"""

from turtle import Turtle

INITIAL_CORD = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class for Snake Game"""

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        """Create the initial snake with three segments"""
        for cord in INITIAL_CORD:
            self.add_snake(cord)

    def add_snake(self, cord):
        """Add a new segment to the snake at the given coordinates"""
        snake = Turtle("circle")
        snake.color("red")
        snake.penup()
        snake.goto(cord)
        self.snake_list.append(snake)

    def extend_snake(self):
        """Extend the snake by adding a new segment at the last segment's position"""
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        """Move the snake forward by updating the position of each segment"""
        for snake in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        """Move the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segments in self.snake_list:
            segments.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
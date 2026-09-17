"""Snake Game"""

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoring import Score

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=400)
screen.bgpic("bg_1.png")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

start_game = True
while start_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Generate food after eating it.
    if snake.head.distance(food) < 15:
        food.generate_food()
        snake.extend_snake()
        scoreboard.calculate_score()

    # Snake collision with wall.
    if (
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 185
        or snake.head.ycor() < -185
    ):
        scoreboard.reset()
        snake.reset()

    # Head and tail collision.
    for snake_body in snake.snake_list[1:]:
        if snake.head.distance(snake_body) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

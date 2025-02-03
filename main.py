from turtle import Turtle, Screen
from snake import Snake
from food import Food
from tailbig import TAILBIG
from scoreboard import SCOREBOARD
import time
snake=Snake()
food=Food()
score=SCOREBOARD()
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
game_on=True
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295:
        # score.reset()
        snake.reset_snake_x()
    elif snake.head.ycor()>295 or snake.head.ycor()<-295:
        # score.reset()
        snake.reset_snake_y()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.increase_size()
        score.increase_score()

    for segments in snake.list_of_square[1:]:
        if snake.head.distance(segments) < 5:
            score.reset()
            snake.new_game()
            snake.reenter()
            # game_on=False













screen.exitonclick()
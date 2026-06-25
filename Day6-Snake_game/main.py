from snake import Snake
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
snake_moving = True

while snake_moving:
    screen.update()
    time.sleep(0.5)
    snake.move()


snake.game_over()







screen.exitonclick()
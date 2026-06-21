import turtle as t
import random

##Spirograph challenge

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)
turtle.speed("fastest")

for i in range(0, 360, 5):
    turtle.circle(100)
    turtle.color(random_color())
    turtle.right(5)

screen.exitonclick()
import turtle as t
import random

##Random walk challenge

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


t.colormode(255)
turtle = t.Turtle()
screen = t.Screen()
turtle.shape("turtle")
screen.bgcolor("black")
turtle.color(random_color())
turtle.pensize(15)
turtle.speed("fastest")
east = 0
north = 90
west = 180
south = 270


for i in range(5000):
    turtle.forward(50)
    turtle.seth(random.choice([east, north, west, south]))
    turtle.color(random_color())










screen.exitonclick()
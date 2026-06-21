from turtle import Turtle, Screen
import random

##Different Shapes challenge - draw different shapes (from triangle to decagon).

possible_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "white"]
turtle = Turtle()
screen = Screen()
turtle.shape("turtle")
screen.bgcolor("black")
turtle.color("red")


triangles = 3

while triangles <= 10:
    for i in range(triangles):
        turtle.forward(100)
        turtle.right(360/triangles)
    triangles += 1
    new_color = random.choice(possible_colors)
    turtle.color(new_color)
    possible_colors.remove(new_color)


screen.exitonclick()
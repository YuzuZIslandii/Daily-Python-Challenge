from turtle import *

##Square challenge - just draw square

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
turtle.pensize(15)
for i in range(4):
    turtle.forward(200)
    turtle.left(90)




screen = Screen()
screen.exitonclick()
from turtle import *
import heroes


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

print(heroes.gen())




screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen

##Dash line challenge - draw dashed line

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("red")
screen.bgcolor("black")

for i in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()




screen.exitonclick()
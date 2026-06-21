import turtle as t
import random

#requirements
#10 by 10 rows of spots
#each dot 20 in size, spaced 50 paces

color_list = [(206, 172, 106), (150, 180, 198), (150, 183, 172), (196, 164, 176), (227, 200, 112), (206, 181, 199), (173, 189, 214), (188, 177, 61), (157, 208, 192), (160, 202, 217), (111, 125, 189), (217, 183, 179), (203, 204, 45), (100, 114, 153)]

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")

current_row = 0
current_col = 0
turtle.setpos(-250, -250)

while current_row < 10:
    while current_col < 10:
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)
        current_col += 1
    turtle.setpos(-250, turtle.ycor() + 50)
    current_col = 0
    current_row += 1

screen.exitonclick()
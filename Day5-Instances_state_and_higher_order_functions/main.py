import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

starting_position = -225, 150
for each in colors:
    new_object = t.Turtle(shape="turtle")
    new_object.color(each)
    new_object.penup()
    new_object.goto(starting_position)
    starting_position = starting_position[0], starting_position[1] - 50
    new_object.speed("fastest")
    turtles.append(new_object)

is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))


        if turtle.xcor() > 225:
            is_race_on = False
            print(f"The winner is {turtle.pencolor()}")
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print("You lost!")
            break


screen.exitonclick()

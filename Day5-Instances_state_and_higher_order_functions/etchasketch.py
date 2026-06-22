import turtle as t

turtle = t.Turtle()
screen = t.Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def move_left():
    turtle.left(10)

def move_right():
    turtle.right(10)

def clear_screen():
    turtle.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
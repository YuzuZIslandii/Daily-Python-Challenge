from turtle import Turtle
class Snake:
    def __init__(self):
        self.starting_position = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(3):
            self.starting_position = (0, 0)
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.speed("fastest")
            self.segments.append(new_segment)
            self.initialize_position()

    def initialize_position(self):
        for segment in range(len(self.segments)):
            self.segments[segment].goto(self.starting_position)
            self.starting_position = self.starting_position[0] - 20, self.starting_position[1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def game_over(self):
        return False
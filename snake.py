from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_part = []
        self.create_snake()
        self.head = self.body_part[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        new_body = Turtle("square")
        new_body.color("black")
        new_body.penup()
        new_body.goto(position)
        self.body_part.append(new_body)

    def extend(self):
        # add new segment
        self.add_body(self.body_part[-1].position())

    def move(self):
        for seg_body in range(len(self.body_part) - 1, 0, -1):
            new_x = self.body_part[seg_body - 1].xcor()
            new_y = self.body_part[seg_body - 1].ycor()
            self.body_part[seg_body].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    #turtle image along with moving
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()
    #turtle to move forwad with a distance of 10
    def move(self):
        self.forward(MOVE_DISTANCE)

    #after reaching the winning line getting back to starting point
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #if it reached finish line say true or false
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
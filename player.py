from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.game_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

#    def go_left(self):
#        self.left(MOVE_DISTANCE)

#    def go_right(self):
#        self.right(MOVE_DISTANCE)

    def game_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

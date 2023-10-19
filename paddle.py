from turtle import Turtle, Screen

STARTING_POSITION_PLAYER_1 = [(350, 20), (350, 0), (350, -20)]
STARTING_POSITION_PLAYER_2 = [(280, 20), (280, 0), (280, -20)]

UP = 90
Down = 90

class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.positions = positions
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(self.positions)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def move_up(self):
        new_y = self.ycor() + 20
        if new_y != 240:
            self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        if new_y != -240:
            self.goto(self.xcor(), new_y)






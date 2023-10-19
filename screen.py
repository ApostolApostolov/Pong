from turtle import Turtle

STARTING_POINT = 290
ENDING_POINT = -290
LINE_SIZE = (0.5, 0.3, 0.2)


class Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.line()

        self.penup()
        self.color("white")
        self.hideturtle()

        self.player_1_score = 0
        self.player_2_score = 0
        self.update_scoreboard()


    def line(self):
        current_row = - 290
        while current_row < STARTING_POINT:
            line = Turtle()
            line.penup()
            line.shape("square")
            line.color("white")
            line.speed("fastest")
            line.shapesize(0.6, 0.2, 0.2)
            line.goto(0, current_row)
            current_row += 20

    def update_scoreboard(self):
        self.clear()
        self.goto(x=30, y=270)
        self.write(self.player_1_score, font=('Ariel', 20, 'bold'))

        self.goto(x=-30, y=270)
        self.write(self.player_1_score, font=('Ariel', 20, 'bold'))

    def player_1_score_increase(self):
        self.player_1_score += 1
        self.update_scoreboard()

    def player_2_score_increase(self):
        self.player_2_score += 1
        self.update_scoreboard()


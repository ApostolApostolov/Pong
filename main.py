from turtle import Turtle, Screen
from paddle import Paddle
from screen import Screen as scoreboard
from ball import Ball
import time

BOTTOM_BORDER = (0, -260)
TOP_BORDER = (0, 260)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

playing_area = scoreboard()

paddle_player_1 = Paddle((350, 0))
screen.onkey(paddle_player_1.move_up, "Up")
screen.onkey(paddle_player_1.move_down, "Down")

paddle_player_2 = Paddle((-350, 0))
screen.onkey(paddle_player_2.move_up, "w")
screen.onkey(paddle_player_2.move_down, "s")

ball = Ball()
ball.speed("slow")
screen.update()

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.1)

    # paddle logic
    if (ball.distance(paddle_player_1) < 50 and ball.xcor() > 320) or (ball.distance(paddle_player_2) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.increase_speed()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # scoring
    if ball.xcor() > 380:
        playing_area.player_2_score_increase()
        ball.reset()
        ball.reset_speed()

    if ball.xcor() < -380:
        playing_area.player_1_score_increase()
        ball.reset()
        ball.reset_speed()


screen.exitonclick()

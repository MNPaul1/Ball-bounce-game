from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time 

screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True
ball.speed("fastest")
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #detect the collision
    if ball.ycor() > 280 or ball.ycor()< -280:
        #needs to bounce
        ball.bounce_y()
    
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()

    #detect the miss R
    if ball.xcor()>380 :
        ball.reset_position()
        scoreboard.l_point()

        
    #detect the miss L
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()
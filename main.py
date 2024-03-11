from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("cyan")
screen.title(" Welcome to my classic Snake Game")
screen.tracer(0)

snake= Snake()
food=Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.inccrease_score()



    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on = False
        scoreboard.game_over()








screen.exitonclick()

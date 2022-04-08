from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.bgcolor('black')              # setting up background screen colour
screen.setup(width=600,height=600)
screen.title('SNAKE GAME')
screen.tracer(0)
snake_obj=Snake()                    # creating snake object
food_obj=Food()                      # creating food object
score_obj=Score()                    # creating score object
screen.listen()
screen.onkey(fun=snake_obj.up, key='Up')          #initializing movement key
screen.onkey(fun=snake_obj.down, key='Down')      #initializing movement key
screen.onkey(fun=snake_obj.left, key='Left')      #initializing movement key
screen.onkey(fun=snake_obj.right, key='Right')    #initializing movement key





game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake_obj.move_snake()

    if snake_obj.head.distance(food_obj) < 15:     #checking collision with food
        # turtle.distance(x) returns the distance b/w turtle and x
        food_obj.new_position()  #setting new position for food
        score_obj.add_score()
        snake_obj.extend_snake()


   # checking collision with walls
    if snake_obj.head.xcor() > 290 or  snake_obj.head.xcor() < -290 or snake_obj.head.ycor() > 290 or snake_obj.head.ycor() < -290:
        score_obj.game_over()
        game_on=False

    for segment in snake_obj.segments:
        #checking collision with body
        if segment != snake_obj.head:
            if snake_obj.head.distance(segment)<10:
                game_on=False
                score_obj.game_over()



screen.exitonclick()
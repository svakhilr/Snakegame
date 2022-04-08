from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super() .__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('red')
        self.new_position()


    def new_position(self): #setting new position for food
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        self.goto(new_x, new_y)


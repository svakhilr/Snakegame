from turtle import Turtle
#global variables
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):  #used to create snake body
        for x in POSITIONS:
            self.add_snake(x)


    def move_snake(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()  # x coordinate of previous segment
            new_y = self.segments[segment - 1].ycor()  # y coordinate of previous segment
            self.segments[segment].goto(x=new_x, y=new_y)

        self.head.forward(20)

    def add_snake(self, positions):   # appends  new turtle objects to segment[]
        new_body = Turtle(shape='square')
        new_body.penup()
        new_body.color('white')
        new_body.goto(positions)
        self.segments.append(new_body)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())  #turtle.position(x) returns the current position if x



    def up(self):
        if self.head.heading()!=DOWN:    #turtle.heading() returns position angle
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



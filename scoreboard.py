from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(10,260)
        self.hideturtle() #hides the turtle
        self.display_score()



    def add_score(self): #used to add score
        self.score+=1
        self.clear()
        self.display_score()

    def display_score(self): #used to display score
        self.write(arg=f"SCORE =  {self.score}", align='center', font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg=f"GAME OVER", align='center', font=("Arial", 24, "normal"))
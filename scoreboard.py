from random import random
from turtle import Turtle
from snake import Snake
import random
class SCOREBOARD(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as HighScore:
            self.HScore=int(HighScore.read())
            print(self.HScore)
        self.penup()
        self.score=0
        self.highscore=self.HScore
        self.color("white")
        self.ht()
        self.goto(0,275)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score= {self.score} High Score: {self.highscore}", False, 'center' , ('Arial',12,'normal'))



    def reset(self):
        if self.score>self.HScore:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        # self.increase_score()
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
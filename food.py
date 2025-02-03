from random import random
from turtle import Turtle
from snake import Snake
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        rand_x = random.randint(-285, 285)
        rand_y = random.randint(-285, 285)
        self.goto(rand_x,rand_y)




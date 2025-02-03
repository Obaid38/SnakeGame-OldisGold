x_coord=[(0,0),(-20,0),(-40,0)]
mov_distance=20
up=90
down=270
left=180
right=0
i=2
from turtle import Turtle
class Snake:
    def __init__(self): #attributes
        self.list_of_square=[]
        self.create_snake()
        self.head= self.list_of_square[0]
    def create_snake(self):
        for index in x_coord:
            self.add_segment(index)

    def move(self):
        hm= len(self.list_of_square)
        for seg in range(hm-1, 0, -1):
            newx = self.list_of_square[seg - 1].xcor()
            newy = self.list_of_square[seg - 1].ycor()
            self.list_of_square[seg].goto(newx, newy)
        self.head.forward(mov_distance)
    def add_segment(self,index):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(index)
        self.list_of_square.append(tim)

    def increase_size(self):
        self.add_segment(self.list_of_square[-1].position())
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
    def reset_snake_x(self):
        new_x=self.head.xcor()
        new_x*=-1
        self.head.goto(new_x,self.head.ycor())
    def reset_snake_y(self):
        new_y = self.head.ycor()
        new_y *= -1
        self.head.goto(self.head.xcor(),new_y)
    def reenter(self):
        self.create_snake()
        self.head=self.list_of_square[0]
    def new_game(self):
        self.list_of_square.clear()

        # self.list_of_square.clear()

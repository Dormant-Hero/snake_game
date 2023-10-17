from turtle import Turtle
from screen import Screen

class Snake(Screen):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.snake_speed = 20

    def create_component(self):
        new_segment = Turtle("square")
        new_segment.goto(10000,10000)
        new_segment.color("#72FF13")
        new_segment.penup()
        self.snake_body.append(new_segment)


    def move_forward(self):
         self.snake_body[0].forward(self.snake_speed)

    def face_north(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def face_south(self):
        if self.snake_body[0].heading() != 90:
          self.snake_body[0].setheading(270)

    def face_east(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def face_west(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def snake_stop(self):
        self.snake_speed = 0

    def snake_stop(self):
        self.snake_speed = 0


    def snake_start(self):
        self.snake_speed = 20


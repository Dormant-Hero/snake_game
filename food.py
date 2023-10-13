import random
from screen import Screen
from turtle import Turtle
from music import Music

music = Music()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_objects = []

    def move_food(self):
        screen = Screen()
        x_location = random.randint(0, screen.screen_width - 1280)
        y_location = random.randint(0, screen.screen_height - 720)
        self.food_objects[0].setposition(x_location, y_location)
        music.munch()

    def construct_food(self):
        food = Turtle("circle")
        food.color("red")
        food.penup()
        screen = Screen()
        x_location = random.randint(900, screen.screen_width - 1280)
        y_location = random.randint(600, screen.screen_height - 720)
        food.setposition(x_location, y_location)
        self.food_objects.append(food)


#The snake game itself
from turtle import Turtle



snake = Turtle()
snake.screen.screensize(500, 500)
snake.screen.bgcolor("black")
snake.dot("red")
snake.screen.mainloop()

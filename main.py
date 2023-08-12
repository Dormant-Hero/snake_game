from menu_gui import Menu_Gui
from music import Music
from screen import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

#This object plays music the background and deals with sound
music = Music()

#This object stores the code for the GUI
menu = Menu_Gui()

# This is the screen
if menu.play_game:
    print("Game should start")
    screen = Screen()
    screen.fullscreen()
    snake = Snake()
    food = Food()
    snake.screen.tracer(0)
    scoreboard = Scoreboard()
    food.construct_food()
    snake.create_component()
    snake.create_component()
    snake.create_component()
    snake.create_component()
    snake.create_component()
    snake.create_component()
    snake_head = snake.snake_body[0]
    snake_head.goto(0,0)
    snake.screen.onkey(snake.face_west, "Left")
    snake.screen.onkey(snake.face_east, "Right")
    snake.screen.onkey(snake.face_north, "Up")
    snake.screen.onkey(snake.face_south, "Down")
    snake.screen.listen()
    while True:
        time.sleep(0.03)
        snake.move_forward()
        for number in range(len(snake.snake_body) - 1, 0, -1):
            snake.snake_body[number].setposition(snake.snake_body[number-1].position())
        distance_from_food_x = snake.snake_body[0].xcor() - food.food_objects[0].xcor()
        distance_from_food_y = snake.snake_body[0].ycor() - food.food_objects[0].ycor()
        if 20 > distance_from_food_x > -20 and -20 < distance_from_food_y < 20:
            food.move_food()
            snake.create_component()
            snake.create_component()
            snake.create_component()
            snake.snake_speed += 0.001
            scoreboard.add_score()
            number = 0
        for component in snake.snake_body[2:]:
            distance_from_component_x = snake_head.xcor() - component.xcor()
            distance_from_component_y = snake_head.ycor() - component.ycor()
            # print(f"Snake Head Coord{number} {snake_head.xcor()}, {snake_head.ycor()}")
            # print(f"Component no {number} {component.xcor()}, {component.ycor()}")
            number += 1
            if 5 > distance_from_component_x > -5 and -5 < distance_from_component_y < 5:
                print("game over")
            if snake_head.xcor() > screen.screen_width/2 or snake_head.xcor() < screen.screen_width/-2:
                print("game over")
            if snake_head.ycor() > screen.screen_height / 2 or snake_head.ycor() < screen.screen_height / -2:
                print("game over")

        snake.screen.update()





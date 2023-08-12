#The screen setup for the game
from turtle import Turtle
import tkinter as tk

class Screen(Turtle):
    def __init__(self):
            super().__init__()
            root = tk.Tk()
            scrollbar_width_guess = 30
            scrollbar_height_guess = 30
            self.screen_width = root.winfo_screenwidth() - scrollbar_width_guess
            self.screen_height = root.winfo_screenheight() - scrollbar_height_guess
            root.destroy()
            #the width of scrollbar based of my own experience
            self.screen.screensize(self.screen_width, self.screen_height)
            self.screen.bgcolor("black")


    def fullscreen(self):
        root = self.screen.getcanvas().winfo_toplevel()
        root.attributes('-fullscreen', True)





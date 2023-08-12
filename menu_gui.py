#GUI Setup

import os
import sys

import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Menu_Gui():
    import customtkinter
    def __init__(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        theme_path = resource_path("default_theme.json")
        self.customtkinter.set_default_color_theme(theme_path) # Themes: blue (default), dark-blue, green
        self.app = self.customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.app.geometry("1920x1080")
        self.app.title("snake")
        self.play_game = self.customtkinter.CTkButton(master=self.app, text="Play Game", command=self.play_game,
                                                      fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                                      text_color="black", hover_color="#6EC531", border_color="black",
                                                      corner_radius=1000)
        self.play_game.place(relx=0.5, rely=0.5, anchor=self.customtkinter.CENTER)
        self.highscores = self.customtkinter.CTkButton(master=self.app, text="Highscores",
                                 fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                 text_color="black", hover_color="#6EC531", border_color="black",
                                    corner_radius=1000)
        self.highscores.place(relx=0.5, rely=0.565, anchor=self.customtkinter.CENTER)
        self.options = self.customtkinter.CTkButton(master=self.app, text="  Options   ",
                                 fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                 text_color="black", hover_color="#6EC531", border_color="black",
                                    corner_radius=1000)
        self.options.place(relx=0.5, rely=0.63, anchor=self.customtkinter.CENTER)
        self.app.mainloop()



    def play_game(self):
        self.app.destroy()
        return True







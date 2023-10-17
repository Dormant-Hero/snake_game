#GUI Setup
import os
import sys
import customtkinter
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Menu_Gui():

    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("1920x1080")
        self.app.title("snake")
        self.play_game = customtkinter.CTkButton(master=self.app, text="Play Game", command=self.play_game,
                                                      fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                                      text_color="black", hover_color="#6EC531", border_color="black",
                                                      corner_radius=1000)
        self.play_game.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        self.highscores = customtkinter.CTkButton(master=self.app, text="Highscores",
                                 fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                 text_color="black", hover_color="#6EC531", border_color="black",
                                    corner_radius=1000)
        self.highscores.place(relx=0.5, rely=0.565, anchor=customtkinter.CENTER)
        self.options = customtkinter.CTkButton(master=self.app, text="  Options   ",
                                 fg_color="#72FF13", font=("'Yu Gothic Medium'", 40),
                                 text_color="black", hover_color="#6EC531", border_color="black",
                                    corner_radius=1000)
        self.options.place(relx=0.5, rely=0.63, anchor=customtkinter.CENTER)
        self.app.mainloop()



    def play_game(self):
        self.app.destroy()
        return True

    def escape_menu(self):
        print("game paused")







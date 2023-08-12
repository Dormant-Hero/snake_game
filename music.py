#background music

class Music():
    import pygame
    def __init__(self):
        self.pygame.init()
        self.pygame.mixer.music.load("Music/roll-the-tape.mp3")
        self.pygame.mixer.music.play(loops=-1)






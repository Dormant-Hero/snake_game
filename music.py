#All the sounds of the game are here
import time

import pygame
import os

class Music():
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load("Music/roll-the-tape.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.3)
        self.munch_sound = pygame.mixer.Sound("Music/nom.mp3")

    def munch(self):
        self.munch_sound.play().set_volume(1)







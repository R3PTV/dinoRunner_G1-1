import pygame
from pygame.locals import *
from pygame import mixer

mixer.init()
mixer.music.load('dino_runner/assets/Other/Dino jump Sound.mp3')
def play(self):
    mixer.music.play()
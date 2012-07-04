import pygame
from pygame.locals import *

import time

pygame.init()

#~ gameOverSound = pygame.mixer.Sound('gameover.wav')
gameOverSound = pygame.mixer.Sound('Geese.mp3')
pygame.mixer.music.load('background.mp3')

null = raw_input('Press key to play music')
pygame.mixer.music.play(-1, 0.0)

null = raw_input('Press key to stop music')
pygame.mixer.music.stop()

gameOverSound.play()
time.sleep(5)
gameOverSound.stop()
print("fin")

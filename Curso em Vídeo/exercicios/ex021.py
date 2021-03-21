import pygame
import os

pygame.init()
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'ex021.mp3'))
pygame.mixer.music.play()
pygame.event.wait()
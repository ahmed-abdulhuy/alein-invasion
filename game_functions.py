import sys
import pygame

def check_event():
    """if event quit detected close the game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


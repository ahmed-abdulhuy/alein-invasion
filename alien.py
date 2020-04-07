import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """represent single alien in the fleet"""
    def __init__(self, ai_setting, screen):
        """initialize the alien"""

        super().__init__()
        self.ai_setting = ai_setting
        self.screen = screen

        # Load the alien image and set the rect attribute
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien position
        self.x = float(self.rect.x)

    def update(self):
        """move the alien right"""
        self.x += self.ai_setting.alien_speed * self.ai_setting.fleet_direction
        self.rect.x = self.x

    def check_edge(self):
        """check if the alien hits an edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blit_me(self):
        """blit the alien on the screen"""
        self.screen.blit(self.image, self.rect)

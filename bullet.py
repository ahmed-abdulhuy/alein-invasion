import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """manage the bullet"""
    def __init__(self, screen, ai_setting, ship):
        """initialise the class attributes"""

        super().__init__()

        # add screen attribute to the class
        self.screen = screen

        # creat bullet rect
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # set movement speed
        self.speed_factor = ai_setting.bullet_speed_factor

        # set the bullet color
        self.color = ai_setting.bullet_color

        # store the centerx value in decimal variable
        self.y = float(self.rect.centerx)

    def update(self):
        """launch the bullet"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """blit the bullet"""
        pygame.draw.rect(self.screen, self.color,  self.rect)

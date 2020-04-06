import pygame


class Ship:
    def __init__(self, screen):
        """Intialise the ship and set it's start position"""
        self.screen = screen

        # load the ship image and set it's rect
        self.imge = pygame.image.load('imgs/ship_img.bmp')

        # make rectangle from the ship
        self.rect = self.imge.get_rect()
        self.screen_rect = screen.get_rect()

        # make the ship start at the center buttom in the star
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
       """Draw the ship at it's current location"""

       self.screen.blit(self.imge, self.rect)
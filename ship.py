import pygame


class Ship:
    def __init__(self, screen, ai_setting):
        """Initialise the ship and set it's start position"""
        self.screen = screen

        # load the ship image and set it's rect
        self.img = pygame.image.load('imgs/ship_img.bmp')

        # make rectangle from the ship
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        # make the ship start at the center buttom in the star
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # define the moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # define setting attribute
        self.ai_setting = ai_setting

        # store the centerx value in decimal variable
        self.center = float(self.rect.centerx)

    def update(self, screen_w, scren_h):
        """update the center variable of the ship"""
        if self.moving_right and self.rect.centerx < screen_w:
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.centerx > 0:
            self.center -= self.ai_setting.ship_speed_factor

        # update the ship position
        self.rect.centerx = self.center

    def blitme(self):
       """Draw the ship at it's current location"""

       self.screen.blit(self.img, self.rect)
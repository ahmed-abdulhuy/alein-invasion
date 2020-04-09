import pygame.ftfont


class Button:
    def __init__(self, ai_setting, screen, msg):
        """initialise button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set dimintions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # build the button's rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Teh massage should be prepared once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Tune massage to rendered image and center text at the button"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button then draw the massage"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
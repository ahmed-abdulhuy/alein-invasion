import pygame.ftfont
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """class to report score information"""
    def __init__(self, ai_setting, screen, states):
        """initialize shopkeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.states = states

        # font settings for scoring information
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # prepare initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image"""
        round_score = int(round(self.states.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = int(round(self.states.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.ai_setting.bg_color)

        # Center the high score on the top of the screen
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image"""
        str_level = str(self.states.level)
        self.level_img = self.font.render(str_level, True, self.text_color, self.ai_setting.bg_color)

        # Position the level image in the left
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how miny ships are left"""
        self.ships = Group()
        for ship_number in range(self.states.ship_left):
            ship = Ship(self.screen, self.ai_setting)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw the score on the screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)

        # Draw ships
        self.ships.draw(self.screen)
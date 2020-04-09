class Setting:
    """Class to svae the game setting."""

    def __init__(self):
        self.width = 1200
        self.height = 700
        self.bg_color = (85, 150, 200)

        # ship setting
        self.ship_limit = 3

        # bullet setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (70, 70, 70)
        self.bullets_allowed = 4

        # Aliens setting
        self.alien_drop_speed = 5

        # Speedup rate
        self.speedup_scale = 1.1

        # How quickly the score points increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize the settings that change throw the game"""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed = 1

        # fleet_direction of 1 represent right and -1 represent left
        self.fleet_direction = 1
        
        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase game speed when leveling up score gain of a hit"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

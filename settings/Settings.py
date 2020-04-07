class Setting:
    """Class to svae the game setting."""

    def __init__(self):
        self.width = 1200
        self.height = 700
        self.bg_color = (85, 150, 200)

        # ship setting
        self.ship_speed_factor = 5

        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (70, 70, 70)
        self.bullets_allowed = 300

        # Aliens setting
        self.alien_speed = 1
        self.alien_drop_speed = 10

        # fleet_direction of 1 represent right and -1 represent left
        self.fleet_direction = 1

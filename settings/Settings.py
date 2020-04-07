class Setting:
    """Class to svae the game setting."""

    def __init__(self):
        self.width = 1200
        self.height = 500
        self.bg_color = (84, 150, 250)

        # ship setting
        self.ship_speed_factor = 2

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (70, 70, 70)
        self.bullets_allowed = 2

class GameStates:
    """Track statistics for alien invasion"""

    def __init__(self, ai_setting):
        """initialize statistics"""
        self.ai_setting = ai_setting
        self.rest_states()
        # start game state
        self.game_active = False
        # highest score
        self.high_score = 0

    def rest_states(self):
        """intialize statistics"""
        self.ship_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1
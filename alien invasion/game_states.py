class GameStats:
    """ a class to store game statics"""
    def __init__(self , ai_game) :
        """initialize statics"""
        self.settings = ai_game.settings
        # high score should never restarts
        self.high_score =0
        self.reset_stats()

    def reset_stats(self):
        """initialise stats that you can change during the game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
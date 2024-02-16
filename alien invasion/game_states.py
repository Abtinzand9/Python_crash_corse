class GameStats:
    """ a class to store game statics"""
    def __init__(self , ai_game) :
        """initialize statics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialise stats that you can change during the game"""
        self.ship_left = self.settings.ship_limit
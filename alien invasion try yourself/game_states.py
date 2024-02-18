
class GameStates:
    """a class to save the statics of the game"""
    def __init__(self , ai_game) :
        """initialize the game statics"""
        self.settings = ai_game.settings
        self.restore_settings()

    def restore_settings(self):
        """restore the game statics"""
        self.ship_left = self.settings.ship_limit
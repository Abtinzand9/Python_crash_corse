from pygame import font

class ScoreBoared:
    """ A class to report scoring informations"""
    def __init__(self , ai_game):
        """initialize scorekeeping attributes"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.state

        # font settings
        self.text_color = (30 , 30 , 30)
        self.font = font.SysFont(None , 48)

        # prepate th initil score image
        self.prep_score()

    def prep_score(self):
        """turn score to a renderd image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str , True , self.text_color ,self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect =self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 40


    def show_score(self):
        """draw the score to the screen"""
        self.screen.blit(self.score_image , self.score_rect)
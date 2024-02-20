from pygame import font
from pygame.sprite import Group
from ship import Ship


class ScoreBoared:
    """ A class to report scoring informations"""
    def __init__(self , ai_game):
        """initialize scorekeeping attributes"""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.state


        # font settings
        self.text_color = (30 , 30 , 30)
        self.font = font.SysFont(None , 48)

        # prepate th initil score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn score to a renderd image"""
        rounded_score = round(self.stats.score , -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str , True , self.text_color ,self.settings.bg_color)

        #display the score at the top right of the screen
        self.score_rect =self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 40

    def prep_high_score(self):
        """prepare high score to display on the screen"""
        rounded_high_score = round(self.stats.high_score , -1)
        high_score_str = f"{rounded_high_score:,}"
        self.high_score_image = self.font.render(high_score_str , True , self.text_color , self.settings.bg_color)

        # display high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """prepare the level"""
        level_str = str(self.stats.level)

        self.level_image = self.font.render(level_str , True , self.text_color , self.settings.bg_color)

        # display the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.score_rect.bottom +20
        self.level_rect.right =self. score_rect.right

    def prep_ships(self):
        """show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """draw the score , high score ,ships_left to the screen"""
        self.screen.blit(self.score_image , self.score_rect)
        self.screen.blit(self.high_score_image , self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """check if high score needs an update"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
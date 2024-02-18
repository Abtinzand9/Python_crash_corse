import pygame


class Ship():
    """overal class to maintain the ship"""
    def __init__(self, ai_game) :
        """initilize the ship"""
        self.screen = ai_game.screen
        self.settings= ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the picture
        self.image = pygame.image.load('../gitignore/images/ship.bmp')
        self.rect = self.image.get_rect()
        #start new ship at the middel of the right side of screen
        self.rect.midright = self.screen_rect.midright
        # made a flg for moving the ship
        self.moving_up = False
        self.moving_down = False
        #make a float number for ship position
        self.y = float(self.rect.y)
        

    def update(self):
        """update the ship position after pressing keys"""
        if self.moving_up == True and self.rect.top >0 :
            self.y -= self.settings.ship_speed
            self.rect.y = self.y
        if self.moving_down==True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 
            self.rect.y = self.y

    def biltme(self):
        """draw the ship on the screen"""
        self.screen.blit(self.image , self.rect)



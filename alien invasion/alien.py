import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ a class to represent a single alien"""
    def __init__(self,ai_game):
        """initialize the alien class"""
        super().__init__()

        self.screen = ai_game.screen
        self.settigs = ai_game.settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # make the alien at the left corner of the screen 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save the horizontal position of the alien as a float
        self.x = float(self.rect.x)

    def update(self):
        """update the position of the alien"""
        # move the alien right or left
        self.x += self.settigs.alien_speed * self.settigs.fleet_direction
        self.rect.x = self.x

    def check_edgs(self):
        """retuen true if an alien reches the left or right edge"""
        screen_rect = self.screen.get_rect()
        return ( self.rect.right >= screen_rect.right ) or (self.rect.left <= 0)
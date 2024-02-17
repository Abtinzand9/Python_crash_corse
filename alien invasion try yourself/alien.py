import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to maintain aliens"""
    def __init__(self , ai_game):
        """init aliens"""
        super().__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # make the alien at the right top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save a float number for the vertical position of the alien
        self.y = float(self.rect.y)

    def update(self):
        """update the positions of alien"""
        self.y += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= self.screen_rect.bottom) or (self.rect.top <= self.screen_rect.top )
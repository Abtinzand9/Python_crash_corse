import pygame
from pygame.sprite import Sprite

class Bullet (Sprite):
    """a class to manage bullets fired from the ship"""
    def __init__(self,ai_game):
        """create a bullet object at the current location of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #create a bullet rect at (0,0) and the correct location
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet possision as afloat
        self.y = float(self.rect.y)

    def update(self):
        """update the bullet possision to go upward"""
        # update the exact possision of the bullet
        self.y -= self.settings.bullet_speed
        #update the rect possision
        self.rect.y = self.y

    def draw_bullet (self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
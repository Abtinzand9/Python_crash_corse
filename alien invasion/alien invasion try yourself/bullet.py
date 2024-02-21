import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """an overal class to handle bullets"""
    def __init__(self,ai_game):
        """init method"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        #make the new bullet start from the top of the ship
        self.rect = pygame.Rect(0,0,self.settings.bullet_width , self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midleft

        #make a float variable to hold bullet position
        self.x = float(self.rect.x)

    def update(self):
        """make the bullet move """
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen , self.color , self.rect)
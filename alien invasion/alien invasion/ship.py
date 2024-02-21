import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """a class to manage ship"""
    def __init__(self,ai_game):
        """initialize the ship in the middel of screen"""
        super().__init__()
        self.screen = ai_game.screen
        self.secreen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the left bottom of the screen
        self.rect.midbottom = self.secreen_rect.midbottom
        #store a float for the ship exat horizental position
        self.x = float(self.rect.x)
        #moving flag : start with a ship that not moving 
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship position based on moving flag"""
        #updateing the ship's x value not the rect and ensure not to move bhind the screen
        if self.moving_right and self.rect.right < self.secreen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update the rect from the self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the at the current location"""
        self.screen.blit(self.image , self.rect)

    def center_ship(self):
        """recenter the ship"""
        self.rect.midbottom = self.secreen_rect.midbottom
        self.x = self.rect.x
import pygame

class ship:
    """a class to manage ship"""
    def __init__(self,ai_game):
        """initialize the ship in the middel of screen"""
        self.screen = ai_game.screen
        self.secreen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the left bottom of the screen
        self.rect.midbottom = self.secreen_rect.midbottom
        #moving flag : start with a ship that not moving 
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """update the ship position based on moving flag"""
        if self.moving_right:
            self.rect.x +=1 
        elif self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """draw the at the current location"""
        self.screen.blit(self.image , self.rect)
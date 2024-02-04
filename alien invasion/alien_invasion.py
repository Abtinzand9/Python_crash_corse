import sys 
import pygame

from settings import Settings
from ship import ship

class AlienInvasion():
    """overal class to manage game assets and behavior"""

    def __init__(self) :
        """initalize the game and create game behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_heght))
        pygame.display.set_caption("Alien Invation")
        self.ship = ship(self)

    def run_game(self):
        """start the main loop for the game"""
        while(True):

                self._check_events()
                self.ship.update()
                self._update_screen()
                self.clock.tick(60)
        
    def _check_events(self):
        """respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right
                    self.ship.moving_right =True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """update images to the screen and flip the new scrceen"""
        #redraw the screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make the geme instance and run 
    ai = AlienInvasion()
    ai.run_game()


import sys 
import pygame
from settings import Settings

class AlienInvasion():
    """overal class to manage game assets and behavior"""

    def __init__(self) :
        """initalize the game and create game behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.screen_width , self.settings.screen_heght)
        pygame.display.set_caption("Alien Invation")

    def run_game(self):
        """start the main loop for the game"""
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()
                
                #redraw the screen during each loop
                self.screen.fill(self.settings.bg_color)

                # make the most recently drawn screen visible
                pygame.display.flip()
                self.clock.tick(60)
if __name__ == '__main__':
    # make the geme instance and run 
    ai = AlienInvasion()
    ai.run_game()


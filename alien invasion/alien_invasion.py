import sys 
import pygame

from settings import Settings
from ship import ship
from bullet import Bullet

class AlienInvasion():
    """overal class to manage game assets and behavior"""

    def __init__(self) :
        """initalize the game and create game behaviors"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heght = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invation")
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """start the main loop for the game"""
        while(True):

            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

        
        
    def _check_events(self):
        """respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """respond to krypresses"""
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right =True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_s:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullelt()
    def _check_keyup_events(self , event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """update images to the screen and flip the new scrceen"""
        #redraw the screen during: each loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()

    def _fire_bullelt(self):
        """create a new bullet and add it to the gorupe"""
        if len(self.bullets)< self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """ update position of bullets and delete the old ones"""
        self.bullets.update()
        # get rid of the old bullets
        for bulet in self.bullets.copy():
            if bulet.rect.bottom <=0:
                self.bullets.remove(bulet)
    

if __name__ == '__main__':
    # make the geme instance and run 
    ai = AlienInvasion()
    ai.run_game()


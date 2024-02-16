import pygame
import sys 
from settings import settings
from ship import Ship
from bullet import Bullet


class AlienInvasion():
    """ base class """

    def __init__(self) :
        """initialize """
        pygame.init()
        self.settings = settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("alien_invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def rungame(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.biltme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._key_up_events(event)

    def _key_down_events(self,event):
        """a function for handling keydown actions"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.ship.moving_up =True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_f:
            """go to fullscreen mode"""
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_height = self.screen.get_height()
            self.settings.screen_width = self.screen.get_width()
            self.ship = Ship(self)
        elif event.key == pygame.K_s:
            """restore down the screen"""
            self.settings.screen_height = self.settings.defult_screen_heght
            self.settings.screen_width = self.settings.defult_screen_width
            self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
            self.ship = Ship(self)

    def _key_up_events(self,event):
        """a function for handling keyup actions"""
        if event.key == pygame.K_UP:
            self.ship.moving_up =False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        """fire the bullet from the ship"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """make the positon of the bullet updated"""
        self.bullets.update()
        # delete the old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right == 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.rungame()
        
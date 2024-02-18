import pygame
import sys 

from settings import settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self._create_fleet()

    def rungame(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.biltme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
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
        self._check_bullets_aliens_collitions()

    def _check_bullets_aliens_collitions(self):
        """ remove both alien and the bullet when collitions"""
        collitions = pygame.sprite.groupcollide(self.aliens , self.bullets , True , True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_alien(self, x_position , y_position):
        """create alien"""
        # make a new alien
        new_alien = Alien(self)
        # move it to the correct position
        new_alien.rect.y = y_position 
        new_alien.rect.x = x_position
        new_alien.y = new_alien.rect.y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """create a fleet of aliens"""
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        # get the positons of the alien
        alien_width , alien_height = new_alien.rect.size
        current_x , current_y = alien_width , alien_height
        # make rows of alien
        while current_x < (self.settings.screen_width - 4 * alien_width):
            # make a row of alien
            while current_y < (self.settings.screen_height - 2 * alien_height) :
                self._create_alien(current_x , current_y)
                current_y += 2*alien_height
            current_x += 2*alien_width
            current_y = alien_height 

    def _update_alien(self):
        """update the position of aliens"""
        self._check_fleet_edgs()
        self.aliens.update()
            
    def _check_fleet_edgs(self):
        """check if fleet reches the edgs"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._fleet_change_direction()
                break

    def _fleet_change_direction(self):
        """change the fleet direction and move it a bit right"""
        self.settings.fleet_direction *= -1 
        for alien in self.aliens:
            alien.rect.x += self.settings.fleet_move_close

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.rungame()
        
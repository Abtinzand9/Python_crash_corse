import sys 
import pygame
from time import sleep

from settings import Settings
from ship import ship
from bullet import Bullet
from alien import Alien
from game_states import GameStats
from button import Button

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
        #initialise the stats of the game
        self.state = GameStats(self)
        self.ship = ship(self)
        self.play_button = Button(self , "play")
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # for handle game over snarios
        self.game_active = False

    def run_game(self):
        """start the main loop for the game"""
        while(True):

            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

        
        
    def _check_events(self):
        """respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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

    def _check_play_button(self , mouse_pos):
        """start a new game when player click on the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active =True
            self.state.reset_stats()

            # get rid of old aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet 
            self._create_fleet()
            self.ship.center_ship()

    def _update_screen(self):
        """update images to the screen and flip the new scrceen"""
        #redraw the screen during: each loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # draw the play button 
        if not self.game_active:
            self.play_button.draw_button()
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
        #cehck if a bullet hit an alien and delete both 
        self._bullet_ailen_collitions()

    def _bullet_ailen_collitions(self):
        """handle collitons betweeen bullets and ailens"""
        collisions = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)

        #check if all aliens has been shoot make a new fleet
        if not self.aliens:
            #destroy the exiting bullets and make a new fleet
            self.bullets.empty()
            self._create_fleet()
    
    def _create_fleet(self):
        """create a fleet of aliens"""
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        # create aliens untill there is no more room for another
        # and make one alien space betwween two aliens
        # make the rows untill there is 3 alien height left
        alien_width , alien_height = new_alien.rect.size

        current_x , current_y = alien_width , alien_height
        while current_y <(self.settings.screen_heght -3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x , current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self,x_position, y_position):
        """create alien"""
        alien = Alien(self)
        alien.rect.x = x_position
        alien.rect.y = y_position
        alien.x = x_position
        self.aliens.add(alien)

    def _update_aliens(self):
        """update aliens position"""
        self._check_fleet_edge()
        self.aliens.update()
        # check if an alien hits the ship
        if pygame.sprite.spritecollideany(self.ship , self.aliens):
            self._ship_hit()
        # check if an ailen hit the bottom of screen
        self._check_alien_reach_bottom()

    def _ship_hit(self):
        """respond to the ship hit by alien"""
        if self.state.ship_left > 0:
            # decrese the number of ships left
            self.state.ship_left -= 1
            # get rid of the exiting bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            # recenter the ship and create a new fleet
            self.ship.center_ship()
            self._create_fleet()
            # puse the game
            sleep(0.5)
        else :
            self.game_active =False


    def _check_fleet_edge(self):
        """check if an alien reches the edges"""
        for alien in self.aliens.sprites():
            if alien.check_edgs():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_reach_bottom(self):
        """check if an alien reaches the bottom of the screen """
        for ailen in self.aliens.sprites():
            if ailen.rect.bottom >= self.settings.screen_heght:
                # we treat like an ailen hit the ship
                self._ship_hit()
                break

if __name__ == '__main__':
    # make the geme instance and run 
    ai = AlienInvasion()
    ai.run_game()


import sys
from time import sleep

import pygame
import random

from ships_aliens_img import *
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ships import Ship, SecondShip
from bullets import FirstBullet, SecondBullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavoir."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 640))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
        self.second_bg_img = pygame.transform.smoothscale(self.settings.second_bg_img, self.screen.get_size())
        pygame.display.set_caption("Alien Invasion")
        self.sound = pygame.mixer.Sound('fire.wav')

        #Create an instance to store game statistics,
        #and create a scoreboard.
        self.stats = GameStats(self)
        self.second_stats = GameStats(self)
        self.sb = ScoreBoard(self)


        self.ship = Ship(self, 0, 0)
        self.second_ship = SecondShip(self, 0, 0)
        self.bullets = pygame.sprite.Group()
        self.second_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        #Make the Play button.
        self.play_button = Button(self, "Play")


    def run_game(self):
            """Store the main loop for the game."""
            running = True
            i = 0
            while running:
                if self.stats.level == 3:
                    self.bg_img = self.second_bg_img
                self.screen.blit(self.bg_img, [0,i])
                self.screen.blit(self.bg_img, [0, i  - self.settings.screen_height])
                if i >= self.settings.screen_height:
                    i = 0
                i += 1

                self._check_events()

                if self.stats.game_active:
                    self.ship.update()
                    self.second_ship.update() 
                    self._update_bullets()
                    self._update_aliens()
                        
                self._update_screen()



    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Star a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            #Reset the game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.second_stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Get rid of an remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            self.second_bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            self.second_ship.center_ship()

            #Hide the mouse cursor.
            pygame.mouse.set_visible(False)             

    def _check_keydown_events(self,event):
        """Respod to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_first_bullet()
            self.sound.play()
        elif event.key == pygame.K_e:
            self._fire_second_bullet()
            self.sound.play()
        elif event.key == pygame.K_a:
            self.second_ship.moving_left = True
        elif event.key == pygame.K_d:
            self.second_ship.moving_right = True
        elif event.key == pygame.K_w:
            self.second_ship.moving_upp = True
        elif event.key == pygame.K_s:
            self.second_ship.moving_downn = True
        elif event.key == pygame.K_KP1:
            self.ship.image = images[0]
        elif event.key == pygame.K_KP2:
            self.ship.image = images[1]
        elif event.key == pygame.K_KP3:
            self.ship.image = images[2]
        elif event.key == pygame.K_1:
            self.second_ship.image = images[3]
        elif event.key == pygame.K_2:
            self.second_ship.image = images[4]
        elif event.key == pygame.K_3:
            self.second_ship.image = images[5]
        elif event.key == pygame.K_KP0:
            self.settings.bullet_width += 1
            self.settings.bullet_height += 1
        elif event.key == pygame.K_KP_PLUS:
            self.settings.bullet_width += 2
        elif event.key == pygame.K_z:
            self.settings.second_bullet_width += 1
            self.settings.second_bullet_height += 1
        elif event.key == pygame.K_x:
            self.settings.second_bullet_width += 2

            

    def _check_keyup_events(self,event):
        """Respot to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame. K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_d:
            self.second_ship.moving_right = False
        elif event.key == pygame.K_a:
            self.second_ship.moving_left = False
        elif event.key == pygame.K_w:
            self.second_ship.moving_upp = False
        elif event.key == pygame.K_s:
            self.second_ship.moving_downn = False

    def _fire_first_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = FirstBullet(self)
            self.bullets.add(new_bullet)

    def _fire_second_bullet(self):
        if len(self.second_bullets) < self.settings.bullets_allowed:
            new_bullett = SecondBullet(self)
            self.second_bullets.add(new_bullett)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet positions.
        self.bullets.update()
        self.second_bullets.update()

        #Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        for bullet in self.second_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.second_bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.

        first_ship_collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, False)
        second_ship_collisions = pygame.sprite.groupcollide(
            self.second_bullets, self.aliens, True, False)

        if first_ship_collisions:
            for aliens in first_ship_collisions.values():
                for alien in aliens:
                    if not hasattr(alien, 'hit_count'):
                        alien.hit_count = 1
                    else:
                        alien.hit_count += 1

                    if self.stats.level < 5:
                        if alien.hit_count >= 1:
                            self.aliens.remove(alien)
                            self.stats.score += self.settings.alien_points
                            self.sb.prep_score()
                            self.sb.check_high_score()
                    else:
                        if alien.hit_count >= 2:
                            self.aliens.remove(alien)
                            self.stats.score += self.settings.alien_points
                            self.sb.prep_score()
                            self.sb.check_high_score()

        if second_ship_collisions:
            for aliens in second_ship_collisions.values():
                for alien in aliens:
                    if not hasattr(alien, 'hit_count'):
                        alien.hit_count = 1
                    else:
                        alien.hit_count += 1

                    if self.stats.level < 5:
                        if alien.hit_count >= 1:
                            self.aliens.remove(alien)
                            self.second_stats.second_score += self.settings.alien_points
                            self.sb.prep_score()
                            self.sb.check_high_score()
                    else:
                        if alien.hit_count >= 2:
                            self.aliens.remove(alien)
                            self.second_stats.second_score += self.settings.alien_points
                            self.sb.prep_score()
                            self.sb.check_high_score()


        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _update_aliens(self):
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        if pygame.sprite.spritecollideany(self.second_ship, self.aliens):
            self._second_ship_hit()
        #Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom() 

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Get rid of all remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _second_ship_hit(self):
        if self.stats.ships_left > 0:
            #Decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Get rid of an remaining aliens and bullets.
            self.aliens.empty()
            self.second_bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.second_ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)  


    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create an alien and find the number of aliens in a row.
        #Spacing between each alien is equal to one alien width.
        alien = Alien(self) 
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (1 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                        (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        

    def _create_alien(self,alien_number,row_number):
        #Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

        if self.stats.level // 2 == 0:
            alien.image = aliens_img[0]
        elif self.stats.level // 2 == 1:
            alien.image = aliens_img[1]
        elif self.stats.level // 2 == 2:
            alien.image = aliens_img[2]
        elif self.stats.level // 2 == 3:
            alien.image = aliens_img[3]
        else:
            alien.image = aliens_img[3]
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if an aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break               

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #self.screen.blit(self.settings.bg_img, (0, 0))
        self.ship.blitme()
        self.second_ship.blitme()
        for bullet in self.second_bullets.sprites():
            bullet.draw_bullet()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        #Draw the score information.
        self.sb.show_score()
        #Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()  
        pygame.display.flip()
    
        

if __name__ =='__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

#TODO: Make new aliens/aliens that should be hit 2 times to die

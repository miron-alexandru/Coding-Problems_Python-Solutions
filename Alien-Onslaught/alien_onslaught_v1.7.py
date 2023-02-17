import sys
import random
import pygame
from time import sleep

from ships_aliens_img import aliens_img, ship_images
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard, SecondScoreBoard
from button import Button, MenuButton
from ships import Thunderbird, Phoenix
from bullets import Thunderbolt, Firebird, AlienBullet
from alien import Alien
from power_ups import PowerUp, HealthPowerUp



class StartMenu:
    """A class that manages the start menu"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 640), pygame.RESIZABLE)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Start Menu")
        self.background = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
        self.background_rect = self.background.get_rect()

        # Create buttons
        self.single_player_button = MenuButton(self, "Single Player", 250)
        self.multiplayer_button = MenuButton(self, "Multiplayer", 750)

        self.run_menu()

    def run_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

                # Check if the single player button is clicked
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.single_player_button.rect.collidepoint(mouse_x, mouse_y):
                        # Start single player game
                        single_player_game = SingleplayerAlienOnslaught()
                        single_player_game.run_game()

                # Check if the multiplayer button is clicked
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.multiplayer_button.rect.collidepoint(mouse_x, mouse_y):
                        # Start multiplayer game
                        multiplayer_game = MultiplayerAlienOnslaught()
                        multiplayer_game.run_game()

            # Draw the buttons on the screen
            self.screen.blit(self.background, self.background_rect)
            self.single_player_button.draw_button()
            self.multiplayer_button.draw_button()

            pygame.display.flip()


class MultiplayerAlienOnslaught:
    """Overall class to manage game assets and behavoir for the multiplayer version."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1000, 640), pygame.RESIZABLE)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
        self.reset_bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
        self.second_bg_img = pygame.transform.smoothscale(self.settings.second_bg_img, self.screen.get_size())
        pygame.display.set_caption("Alien Onslaught")
        self.sound = pygame.mixer.Sound('sounds/fire.wav')
        self.last_power_up_time = 0
        self.last_alien_bullet_time = 0

        # Initialize game objects
        self.first_player_ship = Thunderbird(self, 227, 592)
        self.second_player_ship = Phoenix(self, 728, 592)
        self.stats = GameStats(self)
        self.second_stats = GameStats(self)
        self.sb = ScoreBoard(self)
        self.first_player_bullets = pygame.sprite.Group()
        self.second_player_bullets = pygame.sprite.Group()
        self.alien_bullet = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        # Make the Play button.
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Main loop for the game."""
        running = True
        i = 0
        while running:
            if self.stats.level >= 3:
                self.bg_img = self.second_bg_img
            elif self.stats.level <= 1:
                self.bg_img = self.reset_bg_img
            self.screen.blit(self.bg_img, [0,i])
            self.screen.blit(self.bg_img, [0, i  - self.settings.screen_height])
            if i >= self.settings.screen_height:
                i = 0
            i += 1

            self._check_events()

            if self.stats.game_active:
                self._create_power_ups()
                self._update_power_ups()
                self._create_alien_bullets(3)
                self._update_alien_bullets()  
                self._check_alien_bullets_collisions()
                self._check_power_ups_collisions()
                self._update_bullets()
                self._update_aliens()
                self.first_player_ship.update()
                self.second_player_ship.update() 


            self._update_screen()
            

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_height = self.screen.get_rect().height
                self.bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
                self.second_bg_img = pygame.transform.smoothscale(self.settings.second_bg_img, self.screen.get_size())
                self.reset_bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
                self.first_player_ship.screen_rect = self.screen.get_rect()
                self.second_player_ship.screen_rect = self.screen.get_rect()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.second_stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_hp()


            # Get rid of an remaining aliens, bullets and power-ups.
            self.first_player_bullets.empty()
            self.second_player_bullets.empty()
            self.alien_bullet.empty()
            self.power_ups.empty()
            self.aliens.empty()

            # Create a new fleet and center the ships.
            self._create_fleet()
            self.first_player_ship.center_ship()
            self.second_player_ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)             


    def _check_keydown_events(self,event):
        """Respod to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.first_player_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.first_player_ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.first_player_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.first_player_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RETURN:
            self._fire_first_player_bullet()
            self.sound.play()
        elif event.key == pygame.K_SPACE:
            self._fire_second_player_bullet()
            self.sound.play()
        elif event.key == pygame.K_a:
            self.second_player_ship.moving_left = True
        elif event.key == pygame.K_d:
            self.second_player_ship.moving_right = True
        elif event.key == pygame.K_w:
            self.second_player_ship.moving_up = True
        elif event.key == pygame.K_s:
            self.second_player_ship.moving_down = True
        elif event.key == pygame.K_KP1:
            self.first_player_ship.image = ship_images[0]
        elif event.key == pygame.K_KP2:
            self.first_player_ship.image = ship_images[1]
        elif event.key == pygame.K_KP3:
            self.first_player_ship.image = ship_images[2]
        elif event.key == pygame.K_1:
            self.second_player_ship.image = ship_images[3]
        elif event.key == pygame.K_2:
            self.second_player_ship.image = ship_images[4]
        elif event.key == pygame.K_3:
            self.second_player_ship.image = ship_images[5]


    def _check_keyup_events(self,event):
        """Respot to key releases."""
        if event.key == pygame.K_RIGHT:
            self.first_player_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.first_player_ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.first_player_ship.moving_up = False
        elif event.key == pygame. K_DOWN:
            self.first_player_ship.moving_down = False
        elif event.key == pygame.K_d:
            self.second_player_ship.moving_right = False
        elif event.key == pygame.K_a:
            self.second_player_ship.moving_left = False
        elif event.key == pygame.K_w:
            self.second_player_ship.moving_up = False
        elif event.key == pygame.K_s:
            self.second_player_ship.moving_down = False


    def _fire_first_player_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.first_player_bullets) < self.settings.first_player_bullets_allowed:
            new_bullet = Thunderbolt(self)
            self.first_player_bullets.add(new_bullet)


    def _fire_second_player_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.second_player_bullets) < self.settings.second_player_bullets_allowed:
            new_bullet = Firebird(self)
            self.second_player_bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.first_player_bullets.update()
        self.second_player_bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.first_player_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.first_player_bullets.remove(bullet)

        for bullet in self.second_player_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.second_player_bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _update_power_ups(self):
        """Update power-ups"""
        self.power_ups.update()
        for power in self.power_ups.copy():
            if power.rect.bottom <=0:
                self.power_ups.remove(power)

    def _update_alien_bullets(self):
        """Update alien bullets"""
        self.alien_bullet.update()
        for bullet in self.alien_bullet.copy():
            if bullet.rect.bottom <= 0:
                self.alien_bullet.remove(bullet)


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        first_player_ship_collisions = pygame.sprite.groupcollide(
            self.first_player_bullets, self.aliens, True, False)
        second_player_ship_collisions = pygame.sprite.groupcollide(
            self.second_player_bullets, self.aliens, True, False)

        # First player collisions
        if first_player_ship_collisions:
            for aliens in first_player_ship_collisions.values():
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

        # Second player collisions
        if second_player_ship_collisions:
            for aliens in second_player_ship_collisions.values():
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
            self.first_player_bullets.empty()
            self.second_player_bullets.empty()
            self.power_ups.empty()
            self.alien_bullet.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _check_power_ups_collisions(self):
        """Check for collision between a ship and a power-up"""
        first_player_collision = pygame.sprite.spritecollideany(self.first_player_ship, self.power_ups)
        second_player_collision = pygame.sprite.spritecollideany(self.second_player_ship, self.power_ups)

        # First player collisions
        if first_player_collision:
            if isinstance(first_player_collision, PowerUp):
                self._first_ship_power_up()
            elif isinstance(first_player_collision, HealthPowerUp):
                self._power_up_health()
            first_player_collision.kill()

        # Second player collisions
        if second_player_collision:
            if isinstance(second_player_collision, PowerUp):
                self._second_ship_power_up()
            elif isinstance(second_player_collision, HealthPowerUp):
                self._power_up_health()
            second_player_collision.kill()


    def _update_player_settings(self, player_settings):
        """Updates player settings"""
        power_up_choice = random.randint(1, 3)
        if power_up_choice == 1:
            player_settings['bullet_speed'] += 0.5
        elif power_up_choice == 2:
            player_settings['ship_speed'] += 0.5

    def _first_ship_power_up(self):
        """Powers up the first player ship"""
        self._update_player_settings({'bullet_speed': self.settings.first_player_bullet_speed,
                                      'ship_speed': self.settings.first_player_ship_speed})

    def _second_ship_power_up(self):
        """Powers up the second player ship"""
        self._update_player_settings({'bullet_speed': self.settings.second_player_bullet_speed,
                                      'ship_speed': self.settings.second_player_ship_speed})


    def _power_up_health(self):
        """Increases the health of the players"""
        if self.stats.ships_left < self.settings.max_ships:
            self.stats.ships_left += 1
            self.sb.prep_hp()


    def _check_alien_bullets_collisions(self):
        """Manages collisions between the alien bullets and the players"""
        first_player_collision = pygame.sprite.spritecollideany(self.first_player_ship, self.alien_bullet)
        second_player_collision = pygame.sprite.spritecollideany(self.second_player_ship, self.alien_bullet)

        if first_player_collision:
            self._first_player_ship_hit()
            first_player_collision.kill()

        if second_player_collision:
            self._second_player_ship_hit()
            second_player_collision.kill()


    def _first_player_ship_hit(self):
        """Respond to the first player ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_hp()

            self.first_player_bullets.empty()
            self.first_player_ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _second_player_ship_hit(self):
        """Respond to the second player ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_hp()

            self.second_player_bullets.empty()
            self.second_player_ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)  


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        alien = Alien(self) 
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (1 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.first_player_ship.rect.height
        available_space_y = (self.settings.screen_height -
                        (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

        if random.random() < alien.bullet_chance:
            self._create_alien_bullet(alien)

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


    def _update_aliens(self):
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.first_player_ship, self.aliens):
            self._first_player_ship_hit()
        if pygame.sprite.spritecollideany(self.second_player_ship, self.aliens):
            self._second_player_ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom() 


    def _create_alien_bullet(self, alien):
        """Create an alien bullet at the specified alien rect"""
        bullet = AlienBullet(self)
        bullet.rect.centerx = alien.rect.centerx
        bullet.rect.bottom = alien.rect.bottom
        self.alien_bullet.add(bullet)
        

    def _create_alien_bullets(self, num_bullets):
        """Create a certain number of bullets at a certain time"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_alien_bullet_time >= 4000:
            self.last_alien_bullet_time = current_time
            aliens = random.sample(self.aliens.sprites(), k=min(num_bullets, len(self.aliens.sprites())))
            for alien in aliens:
                if alien.last_bullet_time == 0 or current_time - alien.last_bullet_time >= 5000:
                    alien.last_bullet_time = current_time
                    self._create_alien_bullet(alien)


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
                self._first_player_ship_hit()
                break               


    def _create_power_up(self):
        """Create a random power up"""
        if random.randint(0, 1) == 0:
            power_up = HealthPowerUp(self)
        else:
            power_up = PowerUp(self)
        power_up.rect.x = random.randint(0, self.settings.screen_width - power_up.rect.width)
        power_up.rect.y = random.randint(-100, -40)
        self.power_ups.add(power_up)


    def _create_power_ups(self):
        """Create multiple power ups after a certain time has passed"""
        if self.last_power_up_time == 0:
            self.last_power_up_time = pygame.time.get_ticks()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_power_up_time >= random.randint(5000, 10000):
            self.last_power_up_time = current_time
            self._create_power_up()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.first_player_ship.blitme()
        self.second_player_ship.blitme()

        for bullet in self.second_player_bullets.sprites():
            bullet.draw_bullet()

        for bullet in self.first_player_bullets.sprites():
            bullet.draw_bullet()

        for bullet in self.alien_bullet.sprites():
            bullet.draw_bullet()

        for power_up in self.power_ups.sprites():
            power_up.draw_powerup()

        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    


class SingleplayerAlienOnslaught(MultiplayerAlienOnslaught):
    """A class that manages the Singleplayer version of the game"""
    def __init__(self):
        super().__init__()
        self.sb = SecondScoreBoard(self)

    def run_game(self):
        """Main loop of the game"""
        running = True
        i = 0
        while running:
            if self.stats.level == 3:
                self.bg_img = self.second_bg_img
            elif self.stats.level == 1:
                self.bg_img = self.reset_bg_img
            self.screen.blit(self.bg_img, [0,i])
            self.screen.blit(self.bg_img, [0, i  - self.settings.screen_height])
            if i >= self.settings.screen_height:
                i = 0
            i += 1

            self._check_events()

            if self.stats.game_active:
                self._create_power_ups()
                self._update_power_ups()
                self._create_alien_bullets(3)
                self._update_alien_bullets()  
                self._check_alien_bullets_collisions()
                self._check_power_ups_collisions()
                self._update_bullets()
                self._update_aliens()
                self.first_player_ship.update() 

            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_height = self.screen.get_rect().height
                self.bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
                self.second_bg_img = pygame.transform.smoothscale(self.settings.second_bg_img, self.screen.get_size())
                self.reset_bg_img = pygame.transform.smoothscale(self.settings.bg_img, self.screen.get_size())
                self.first_player_ship.screen_rect = self.screen.get_rect()
                
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
            # Reset the game statistics.
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_hp()

            # Get rid of the remaining aliens, bullets and power ups
            self.first_player_bullets.empty()
            self.power_ups.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.first_player_ship.center_ship()

            pygame.mouse.set_visible(False)    




    def _check_keydown_events(self,event):
        """Respod to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.first_player_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.first_player_ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.first_player_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.first_player_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RETURN:
            self._fire_first_player_bullet()
            self.sound.play()
        elif event.key == pygame.K_KP1:
            self.first_player_ship.image = ship_images[0]
        elif event.key == pygame.K_KP2:
            self.first_player_ship.image = ship_images[1]
        elif event.key == pygame.K_KP3:
            self.first_player_ship.image = ship_images[2]


    def _check_keyup_events(self,event):
        """Respot to key releases."""
        if event.key == pygame.K_RIGHT:
            self.first_player_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.first_player_ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.first_player_ship.moving_up = False
        elif event.key == pygame. K_DOWN:
            self.first_player_ship.moving_down = False

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.first_player_bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.first_player_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.first_player_bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.

        first_player_ship_collisions = pygame.sprite.groupcollide(
            self.first_player_bullets, self.aliens, True, False)

        if first_player_ship_collisions:
            for aliens in first_player_ship_collisions.values():
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

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.first_player_bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_power_ups_collisions(self):
        """Check for collision between a ship and a power-up"""
        collision = pygame.sprite.spritecollideany(self.first_player_ship, self.power_ups)

        if collision:
            self.first_player_ship.power_up()
            collision.kill()


    def _update_aliens(self):
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.first_player_ship, self.aliens):
            self._first_player_ship_hit()
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom() 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.first_player_ship.blitme()

        for bullet in self.first_player_bullets.sprites():
            bullet.draw_bullet()

        for power_up in self.power_ups.sprites():
            power_up.draw_powerup()

        for bullet in self.alien_bullet.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ =='__main__':
    start = StartMenu()
    start.run_menu()




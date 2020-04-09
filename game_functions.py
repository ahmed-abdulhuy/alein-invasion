import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_event(ship, bullets, event, ai_setting, screen):
    """check if a left or right  key is pressed """
    if event.key == pygame.K_RIGHT:
        # move the ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # moving the ship to left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # soot the bullet
        fire_bullet(ai_setting, bullets, ship, screen)
    elif event.key == pygame.K_q:
        # exit from the game
        sys.exit()


def fire_bullet(ai_setting, bullets, ship, screen):
    """fire the bullet if allowed"""
    if len(bullets) < ai_setting.bullets_allowed:
        # creat new bullet add it to group
        new_bullet = Bullet(screen, ai_setting, ship)
        bullets.add(new_bullet)


def check_keyup_event(ship, event):
    """check if a left or right  key is depressed """
    if event.key == pygame.K_RIGHT:
        # stop move the ship to right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop moving the ship to left
        ship.moving_left = False


def check_event(ship, bullets, aliens, screen, ai_setting, states, play_button, sb):
    """events handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(ship, bullets, event, ai_setting, screen)

        elif event.type == pygame.KEYUP:
            check_keyup_event(ship, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, states, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y)


def check_play_button(ai_setting, screen, states, sb, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """start game if play is brassed"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not states.game_active:
        # reset the game setting
        ai_setting.initialize_dynamic_setting()

        # Hide mouse
        pygame.mouse.set_visible(False)

        # Reset the game statistics
        states.rest_states()
        states.game_active = True

        # reset score board
        sb.prep_high_score()
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the screen from aliens and bullets
        bullets.empty()
        aliens.empty()

        # Creat fleet and center the ship
        creat_fleet(aliens, ship, screen, ai_setting)
        ship.center_ship()


def check_fleet_edge(ai_setting, aliens):
    """Respond if an alien hits an edge"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_setting, aliens)
            break


def change_fleet_direction(ai_setting, aliens):
    """Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(screen, ai_setting, states, sb, ship, bullets, aliens):
    """respond to collision between ship and alien"""
    if states.ship_left > 1:
        # Decrement ships left
        states.ship_left -= 1

        # Update score board
        sb.prep_ships()

        # Empty the fleet and the bullets
        bullets.empty()
        aliens.empty()

        # Creat new fleet and center the ship
        creat_fleet(aliens, ship, screen, ai_setting)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        states.game_active = False
        pygame.mouse.set_visible(True)


def update_screen(screen, ai_setting, states, sb, ship, bullets, aliens, play_button):
    """update the image and flip hte screen"""
    # Add the background color
    screen.fill(ai_setting.bg_color)

    # blit the ship on te screen
    ship.blitme()

    # redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw aliens
    aliens.draw(screen)

    # Draw sore board
    sb.show_score()

    # Draw play button
    if not states.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullet(ai_setting, screen, states, sb, ship, bullets, aliens):
    """update and get rid of bullets"""
    # Update bullet position
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_alien_bullet_collision(bullets, aliens, ship, screen, ai_setting, states, sb)


def check_alien_bullet_collision(bullets, aliens, ship, screen, ai_setting, states, sb):
    """Respond to alien bullet collision"""
    # Check if a bullet hits an alien
    # If so, get ride of them booth.
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Check if the fleet is destroyed
    # and make another fleet
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()

        # start a new level
        states.level += 1
        sb.prep_level()
        creat_fleet(aliens, ship, screen, ai_setting)

    for aline in collision.values():
        # Increase score when collision happened
        if collision:
            states.score += ai_setting.alien_points * len(aline)
            sb.prep_score()
            check_high_score(states, sb)


def check_alien_bottom(screen, ai_setting, states, sb, ship, aliens, bullets):
    """check if an alien reach the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same way as the ship had been heated
            ship_hit(screen, ai_setting, states, sb, ship, bullets, aliens)
            break


def check_high_score(states, sb):
    """Check if ther is a new high score"""
    if states.high_score < states.score:
        states.high_score = states.score
        sb.prep_high_score()


def update_aliens(screen, ai_setting, states, sb,  aliens, ship, bullets):
    """Check if the fleet hits an edge, and then update the position of the entire fleet"""
    check_fleet_edge(ai_setting, aliens)
    aliens.update()

    # Check aline ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ai_setting, states, sb, ship, bullets, aliens)
    # Check if an alien hits hte screen
    check_alien_bottom(screen, ai_setting, states, sb, ship, aliens, bullets)


def get_number_aliens_x(ai_setting, alien_width):
    """find the number of aliens in a row."""
    # Spaces between aliens equal one alien width.
    available_space_x = ai_setting.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_of_rows(ai_setting, ship_height, alien_height):
    """determine the number of rows fet into the screen"""
    available_space_y = ai_setting.height - (3 * alien_height) - ship_height
    number_of_rows = int(available_space_y / (2 * alien_height))

    return number_of_rows


def creat_alien(screen, ai_setting, aliens, alien_number, row_number):
    """creat an alien and place it in the row"""
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def creat_fleet(aliens, ship,  screen, ai_setting):
    """Creat a full alien's fleet"""
    alien = Alien(ai_setting, screen)

    # Get the number of aliens in a row
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    # Get number fo rows
    number_rows = get_number_of_rows(ai_setting, ship.rect.height, alien.rect.height)
    # Creat the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Creat an alien and palace in the row
            creat_alien(screen, ai_setting, aliens, alien_number, row_number)

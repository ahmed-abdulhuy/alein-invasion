import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def check_event(ship, bullets, screen, ai_setting):
    """events handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(ship, bullets, event, ai_setting, screen)

        elif event.type == pygame.KEYUP:
            check_keyup_event(ship, event)


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


def update_screen(screen, ai_setting, ship, bullets, aliens):
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

    pygame.display.flip()


def update_bullet(ai_setting, screen, ship, bullets, aliens):
    """update and get rid of bullets"""
    # Update bullet position
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check if a bullet hits an alien
    # If so, get ride of them booth.
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Check if the fleet is destroyed
    # and make another fleet
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(aliens, ship, screen, ai_setting)


def update_aliens(ai_setting, aliens):
    """Check if the fleet hits an edge, and then update the position of the entire fleet"""
    check_fleet_edge(ai_setting, aliens)
    aliens.update()


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

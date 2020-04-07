import sys
import pygame
from bullet import Bullet


def check_keydown_event(ship, bullets, event, ai_setting, screen):
    """check if a left or right  key is pressed """
    if event.key == pygame.K_RIGHT:
        # move the ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # moving the ship to left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE and len(bullets) < ai_setting.bullets_allowed:
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


def update_screen(screen, ai_setting, ship, bullets):
    """update the image and flip hte screen"""
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # redraw all bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()


def update_bullet(bullets):
    """update and get rid of bullets"""
    # Update bullet position
    bullets.update()

    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

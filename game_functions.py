import sys
import pygame


def check_keydown_event(ship, event):
    """check if a left or right  key is pressed """
    if event.key == pygame.K_RIGHT:
        # move the ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # moving the ship to left
        ship.moving_left = True


def check_keyup_event(ship, event):
    """check if a left or right  key is depressed """
    if event.key == pygame.K_RIGHT:
        # stop move the ship to right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop moving the ship to left
        ship.moving_left = False


def check_event(ship):
    """events handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(ship, event)
        elif event.type == pygame.KEYUP:
            check_keyup_event(ship, event)


def update_screen(screen, ai_setting, ship):
    """update the image and flip hte screen"""
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    pygame.display.flip()


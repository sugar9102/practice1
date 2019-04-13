import sys
import pygame
from cyclone import Cyclone


def check_keydown_events(event, yasuo):
    """响应按键"""
    if event.key == pygame.K_UP:
        """向上移动亚索"""
        yasuo.moving_up = True
    elif event.key == pygame.K_DOWN:
        """向下移动亚索"""
        yasuo.moving_down = True
    elif event.key == pygame.K_LEFT:
        """向左移动亚索"""
        yasuo.moving_left = True
    elif event.key == pygame.K_RIGHT:
        """向右移动亚索"""
        yasuo.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, yasuo):
    """响应松开"""
    if event.key == pygame.K_UP:
        """向上移动亚索"""
        yasuo.moving_up = False
    elif event.key == pygame.K_DOWN:
        """向下移动亚索"""
        yasuo.moving_down = False
    elif event.key == pygame.K_LEFT:
        """向左移动亚索"""
        yasuo.moving_left = False
    elif event.key == pygame.K_RIGHT:
        """向右移动亚索"""
        yasuo.moving_right = False


def check_events(yasuo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #check_keydown_events(event, ai_settings, screen, yasuo)
            check_keydown_events(event, yasuo)
        elif event.type  == pygame.KEYUP:
            check_keyup_events(event, yasuo)


def update_screen(ai_settings, screen, yasuo, cyclone):
    screen.fill(ai_settings.bg_color)

    yasuo.blitme()
    cyclone.blitme()

    pygame.display.flip()
import sys
import pygame
from settings import Settings
from yasuo import Yasuo
from cyclone import Cyclone
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("yasuo is coming...")

    yasuo = Yasuo(ai_settings, screen)
    cyclone = Cyclone(ai_settings, screen, yasuo)

    while True:
        "监视键盘和鼠标事件3"
        #gf.check_events(ai_settings, screen, yasuo)
        gf.check_events(yasuo)

        yasuo.update()
        cyclone.update()

        gf.update_screen(ai_settings, screen, yasuo, cyclone)


run_game()
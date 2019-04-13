import sys
import pygame


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("blue screen")
    bg_color = (255, 255, 255)

    while True:
        "监视键盘和鼠标事件3"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()


create_screen()

import pygame
#from pygame.sprite import Sprite


class Cyclone():
    def __init__(self, ai_settings, screen, yasuo):
        """在亚索所处的位置创建一个旋风对象"""
        super(Cyclone, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.yasuo = yasuo

        """加载旋风图像并获得其外接矩形及屏幕外接矩形及亚索外接矩形"""
        self.image = pygame.image.load('images/cyclone_white.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.yasuo_rect = yasuo.rect

        """将旋风放在亚索左侧"""
        self.rect.right = self.yasuo_rect.left
        self.rect.bottom = self.yasuo_rect.bottom

        """存储用小数表示的旋风位置"""
        self.x = float(self.rect.x)

        """旋风移动速度"""
        self.speed_factor = ai_settings.cyclone_speed_factor

    def update(self):
        """向左移动旋风"""
        """更新表示旋风位置的小数值"""
        if self.rect.x >= 0:
            self.x -= self.speed_factor
        """更新表示旋风的rect位置"""
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制旋风"""
        self.screen.blit(self.image, self.rect)
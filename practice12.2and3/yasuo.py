import pygame


class Yasuo():
    def __init__(self, ai_settings, screen):
        """初始化亚索并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        """加载亚索图像并获得其外接矩形及屏幕外接矩形"""
        self.image = pygame.image.load('images/yasuo.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """将亚索放在屏幕右侧中央"""
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        """移动标志"""
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        """在亚索的属性center中存储小数值"""
        self.center = float(self.rect.centery)
        self.center1 = float(self.rect.centerx)



    def update(self):
        """根据移动标志更新飞船的位置"""
        if self.moving_up and self.rect.top >= 0:
            self.center -= self.ai_settings.yasuo_speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center += self.ai_settings.yasuo_speed_factor
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center1 += self.ai_settings.yasuo_speed_factor_left_right
        if self.moving_left and self.rect.left >= 0:
            self.center1 -= self.ai_settings.yasuo_speed_factor_left_right
        """根据self.center更新rect对象"""
        self.rect.centery = self.center
        self.rect.centerx = self.center1

    def blitme(self):
        """在指定位置绘制亚索"""
        self.screen.blit(self.image, self.rect)



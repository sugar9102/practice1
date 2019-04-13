class Settings():
    """存储亚索的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        """亚索的初始化设置"""
        self.yasuo_speed_factor = 1.5
        self.yasuo_speed_factor_left_right = 3

        """旋风的初始化设置"""
        self.cyclone_speed_factor = 3
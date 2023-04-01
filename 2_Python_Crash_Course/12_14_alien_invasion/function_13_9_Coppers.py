import pygame
from pygame.sprite import Sprite


class Coppers(Sprite):
    """一个关于铜钱的类"""
    def __init__(self, cc_settings, screen) -> None:
        """初始化参数"""
        super(Coppers,self).__init__()
        self.cc_settings = cc_settings
        self.screen = screen

        # 加载铜钱图像和图像参数
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\coppers.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化铜钱的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """把铜钱绘制到屏幕上"""
        self.screen.blit(self.image,self.rect)

    def check_bottom(self):
        """检测铜钱是否触底"""
        if self.rect.bottom > self.screen_rect.bottom:
            return True
    
    def update(self):
        """让铜钱下落"""
        self.y += self.cc_settings.copper_drop_speed
        self.rect.y = self.y
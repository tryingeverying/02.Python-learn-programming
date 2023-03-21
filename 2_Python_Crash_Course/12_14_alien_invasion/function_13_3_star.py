"""一个关于星星的类"""
import pygame
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self,star_setting,screen):
        """初始化屏幕和设置类"""
        super(Star, self).__init__()
        self.screen = screen
        self.star_setting = star_setting
        # 导入图片并且获取图片的外接矩形
        self.image = pygame.image.load(r"02.Python-learn-programming\2_Python_Crash_Course\12_14_alien_invasion\images\star.bmp")
        self.rect = self.image.get_rect()
        # 将图片的初始位置放置在屏幕上
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 图片的坐标值可以是小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # 将星星图片绘制到屏幕的rect位置
        self.screen.blit(self.image, self.rect)
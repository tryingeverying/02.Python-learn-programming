"""一个关于雨滴的类"""
from pygame.sprite import Sprite
import pygame

class RainDrop(Sprite):
    """一个关于雨滴的类"""
    def __init__(self, rain_setting,screen) -> None:
        super(RainDrop, self).__init__()
        self.screen = screen
        self.rain_setting = rain_setting
        # 导入图片，并且通过get_rect方法获取其外接矩形
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\raindrop.bmp")
        self.rect = self.image.get_rect()
        # 图片出现的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 将图片的初始位置设定为可以是float
        self.x = float(self.rect.x )
        self.y = float(self.rect.y )

    def blitme(self):
        # 将图片绘制到屏幕上
        self.screen.blit(self.image,self.rect)

    def check_edge(self):
        # 检测雨滴是否到达屏幕的底部
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.bottom:
            return True

    def update(self):
        # 雨滴往下掉落
        self.y += self.rain_setting.rain_speed_factor
        self.rect.y = self.y















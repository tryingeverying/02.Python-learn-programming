import pygame
from pygame.sprite import Sprite


class GoldToad(Sprite):
    """定义一个关于金蟾的类"""
    def __init__(self, cc_settings, screen) -> None:
        super(GoldToad,self).__init__()
        self.cc_settings = cc_settings
        self.screen = screen

        # 加载金蟾的图像以及图像信息
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\goldtoad.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 确定金蟾的初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.x = self.screen_rect.centerx
        # self.rect.y= self.screen_rect.bottom
        # pygame里的xy值指的是图上的左上角，
        # 如上面那种写法图片的左上角的横坐标是屏幕的中心，
        # 图像左上角的纵坐标是屏幕的底部,
        # 也就是说图像左上角的坐标是屏幕底边的中点，
        # 图像整个都在屏幕下面了，屏幕上肯定没有图像显示了
        # 精确化金蟾的横坐标
        self.x = float(self.rect.centerx)
        # 移动判断符
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """使得金蟾可以左右移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.cc_settings.toad_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.cc_settings.toad_speed_factor
        self.rect.centerx = self.x

    def blitme(self):
        """将金蝉的图像绘制到屏幕上"""
        self.screen.blit(self.image,self.rect)

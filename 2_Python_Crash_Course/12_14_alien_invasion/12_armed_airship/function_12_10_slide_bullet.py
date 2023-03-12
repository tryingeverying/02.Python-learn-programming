import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对火箭发射的子弹进行管理"""
    def __init__(self,ai_setting,screen,rocket) -> None:
        """在火箭所处的位置处创建一个子弹"""
        super(Bullet,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,ai_setting.bullet_height,
                                ai_setting.bullet_width)
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery
        # 把飞船的中心的横坐标和飞船顶部的纵坐标赋值给子弹的中心和顶部

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.right)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
    
    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数点
        self.x += self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.right = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)









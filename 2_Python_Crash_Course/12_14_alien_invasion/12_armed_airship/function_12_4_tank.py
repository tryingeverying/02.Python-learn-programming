"""创建一个坦克类 """
import pygame

class Tank():

    def __init__(self,screen) -> None:
        """初始化坦克在屏幕中的位置"""
        self.screen = screen

        #外接矩形
        self.image = pygame.image.load(r"02.Python-learn-programming\2_Python_Crash_Course\12_14_alien_invasion\12_armed_airship\images\tank.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将图像放置在屏幕的中心
        self.rect.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制图像"""
        self.screen.blit(self.image,self.rect)









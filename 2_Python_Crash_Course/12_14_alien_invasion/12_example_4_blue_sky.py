"""12-1 蓝色天空 ：创建一个背景为蓝色的Pygame窗口。"""
import sys
import pygame
from function_12_1_setting import Settings

def blue_sky():
    pygame.init()   # 初始化pygame
    sky_setting = Settings()
    screen = pygame.display.set_mode((sky_setting.screen_width,sky_setting.screen_height))
    pygame.display.set_caption("蓝色天空")

    screen.fill(sky_setting.bg_color)

    while True:
        # 监视键盘和鼠标的操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

blue_sky()









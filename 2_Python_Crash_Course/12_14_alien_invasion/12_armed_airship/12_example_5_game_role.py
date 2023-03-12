"""12-2 游戏角色 ：找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。
创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，
或将屏幕背景色设置为该图像的背景色。"""
import sys
import pygame
from function_12_1_setting import Settings
from function_12_4_tank import Tank

def tank_game():
    pygame.init()   # 初始化pygame
    tank_setting = Settings()
    screen = pygame.display.set_mode((tank_setting.screen_width,tank_setting.screen_height))
    pygame.display.set_caption("坦克战争")

    # 创建一艘飞船
    tank = Tank(screen)
    
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标的操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕 
        screen.fill(tank_setting.bg_color)  
        tank.blitme() 
        # 用背景色填充屏幕；这个方法只接受一个实参：一种颜色。

        # 让最近绘制的屏幕可见
        pygame.display.flip()

tank_game()
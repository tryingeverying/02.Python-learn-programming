import sys
import pygame
from function_12_1_setting import Settings
from function_12_2_ship import Ship

def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(screen)
    
    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标的操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕 
        screen.fill(ai_setting.bg_color)  
        ship.blitme() 
        # 用背景色填充屏幕；这个方法只接受一个实参：一种颜色。

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()













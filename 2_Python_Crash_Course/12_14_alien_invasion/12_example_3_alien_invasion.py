import pygame

from function_12_1_setting import Settings
from function_12_2_ship import Ship
import function_12_3_game_functions as gf

def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(ai_setting,screen)

    #开始游戏主循环
    while True:
        # 监视鼠标和键盘的命令
        gf.check_events(ship) 

        # 飞船移动
        ship.update()

        # 更新屏幕图像
        gf.update_screen(ai_setting,screen,ship)

run_game()













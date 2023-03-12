"""12-3 火箭 ：编写一个游戏，开始时屏幕中央有一个火箭，
而玩家可使用四个方向键上下左右移动火箭。
请务必确保火箭不会移到屏幕外面。"""

import pygame
from function_12_1_setting import Settings
from function_12_6_rocket import Rocket
import function_12_7_rocket_functions as rf

def rocket_game():
    """初始化游戏界面"""
    pygame.init()
    rocket_settings = Settings()
    screen = pygame.display.set_mode(
        (rocket_settings.screen_width,rocket_settings.screen_height)
    )
    pygame.display.set_caption("火箭游戏")

    # 初始化火箭对象
    rocket = Rocket(rocket_settings,screen)

    # 开始游戏循环
    while True:
        # 监视键盘和鼠标
        rf.check_events(rocket)

        # 火箭的上下左右移动
        rocket.update()

        # 绘制图像
        rf.update_screen(rocket_settings,screen,rocket)

rocket_game()


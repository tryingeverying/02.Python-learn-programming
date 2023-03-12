"""12-5 侧面射击 ：编写一个游戏，将一艘飞船放在屏幕左边，
并允许玩家上下移动飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，
并在子弹离开屏幕而消失后将其删除。"""


import pygame
from pygame.sprite import Group
from function_12_1_setting import Settings
from function_12_9_slide_rocket import Rocket
import function_12_11_slide_shoot_functions as rf


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

    # 创建子弹的集合
    bullets = Group()
    # 开始游戏循环
    while True:
        # 监视键盘和鼠标
        rf.check_events(rocket_settings,screen,rocket,bullets)

        # 火箭的上下移动
        rocket.update()
        # 控制子弹
        rf.update_bullets(bullets)
        # 绘制图像
        rf.update_screen(rocket_settings,screen,rocket,bullets)

rocket_game()















import pygame

from pygame.sprite import Group
from function_12_1_setting import Settings
from function_12_2_ship import Ship
import function_12_5_re_game_functions as gf

def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏主循环
    while True:
        # 监视鼠标和键盘的命令
        gf.check_events(ai_settings,screen,ship,bullets) 

        # 飞船移动
        ship.update()
        #控制子弹
        gf.update_bullets(bullets)
        # 更新屏幕图像  
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()













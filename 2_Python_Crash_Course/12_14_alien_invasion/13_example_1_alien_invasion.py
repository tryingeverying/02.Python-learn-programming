import pygame
import sys
from pygame.sprite import Group
from function_12_1_setting import Settings
from function_12_2_ship import Ship
from function_13_11_GameStats import GameStats
import function_13_7_re_game_functions as gf



def run_game():
    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")
    # 创建一个用于存储游戏信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
 
    #开始游戏主循环
    while True:
        # 监视鼠标和键盘的命令
        gf.check_events(ai_settings,screen,ship,bullets) 

        if stats.game_active :
            # 飞船移动
            ship.update()
            #控制子弹
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            #更新外星人
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,)
        else:
            sys.exit()
            
        # 更新屏幕图像  
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)
        

run_game()













import pygame
from pygame.sprite import Group
from function_12_1_setting import Settings
import function_13_4_star_functions as sf

def star_screen():
    """初始化屏幕数据"""
    pygame.init()
    star_setting = Settings()
    screen = pygame.display.set_mode((star_setting.screen_width,
                                     star_setting.screen_height))
    pygame.display.set_caption("星星铺满屏幕")

    # 创建一个星星的编组
    stars = Group()

    sf.create_stars(star_setting,screen,stars)
    while True:
        sf.check_keydown_events()
        # 让最近绘制的屏幕可见
        sf.update_screen(star_setting,screen,stars)

star_screen()








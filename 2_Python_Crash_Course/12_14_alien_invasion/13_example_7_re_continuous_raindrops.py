"""13-4 连绵细雨 ：修改为完成练习13-3而编写的代码，
使得一行雨滴消失在屏幕底端后，屏幕顶端又出现一行新雨滴，并开始往下落。"""

import pygame
from function_12_1_setting import Settings
from pygame.sprite import Group
import function_13_6_rain_function as rf 

def rain_drop():
    rain_setting = Settings()
    screen = pygame.display.set_mode((rain_setting.screen_width,
                                      rain_setting.screen_height))
    # 创建一个雨滴的编组
    rains = Group()
    rf.initialization_functions()
    
    rf.create_rains(rain_setting,screen,rains)
    while True:
        rf.check_events()
        rf.update_rain(rains,rain_setting,screen)
        rf.update_screen(rain_setting,screen,rains)

if  __name__ == "__main__":
    rain_drop()


















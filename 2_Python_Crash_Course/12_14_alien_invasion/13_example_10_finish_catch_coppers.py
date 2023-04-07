"""13-5 抓球 ：创建一个游戏，在屏幕底端放置一个玩家可左右移动的角色。
让一个球出现在屏幕顶端，且水平位置是随机的，并让这个球以固定的速度往下落。
如果角色与球发生碰撞（表示将球抓住了），就让球消失。
每当角色抓住球或球因抵达屏幕底端而消失后，都创建一个新球。
13-6 游戏结束 ：在为完成练习13-5而编写的代码中，
跟踪玩家有多少次未将球接着。在未接着球的次数到达三次后，结束游戏。
"""
import pygame,sys
import function_13_10_function_goldtoad as fg
from pygame.sprite import Group
from function_12_1_setting import Settings
from function_13_12_cc_gamestats import GameStats
def run_game():
    # 初始化pygame,设置以及屏幕
    pygame.init()
    cc_settings = Settings()
    screen = pygame.display.set_mode(
        (cc_settings.screen_width,cc_settings.screen_height)
    )
    pygame.display.set_caption("吞财金蟾")

    # goldtoad = GoldToad(cc_settings,screen)
    goldtoads = Group()
    coppers = Group()

    fg.create_goldtoad(cc_settings,screen,goldtoads)
    fg.create_copper(cc_settings,coppers, screen)
    # 初始化记录游戏信息的对象
    stats = GameStats(cc_settings)
    
    while True:
        if stats.game_active:
            fg.update_location(cc_settings,goldtoads,coppers,screen,stats)
        else:
            sys.exit()
        fg.update_screen(screen,cc_settings,goldtoads,coppers)
        

if __name__ == "__main__":
    run_game()












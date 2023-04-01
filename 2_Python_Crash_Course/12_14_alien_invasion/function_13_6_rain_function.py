"""雨滴下落的控制函数集"""

import sys
import pygame
from function_13_5_RainDrop import RainDrop

# 初始化屏幕
def initialization_functions():
    pygame.init()
    pygame.display.set_caption("连续雨滴掉落")

# 检测按下的键是什么键
def check_keydown_events(event):
    if event.key == pygame.K_q:
        sys.exit()

# 监控键盘的情况
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

# 计算屏幕上一行可以放置多少个雨滴
def get_number_rain_line(rain_setting,rain):
    available_space_line =  rain_setting.screen_width - 2 * rain.rect.width
    number_rain_line = int(available_space_line /(2 * rain.rect.width))
    return number_rain_line
# 计算屏幕上可以放置多少行的雨滴
def get_number_rain_row(rain_setting,rain):
    available_space_row = rain_setting.screen_height - 15 * rain.rect.height
    number_rain_row = int(available_space_row /(2 * rain.rect.height))
    return number_rain_row
# 创建单个雨滴
def create_rain(rain_setting,screen,number_rain_line,number_rain_row,rains):
    rain = RainDrop(rain_setting,screen)
    rain_width = rain.rect.width
    rain_height = rain.rect.height 
    rain.x = rain_width + 2 * rain_width * number_rain_line
    rain.y = rain_height + 2 * rain_height * number_rain_row
    rain.rect.x = rain.x
    rain.rect.y = rain.y
    # 把生成的新的雨滴传入雨滴的编组
    rains.add(rain)
# 创建有序排列的雨滴编组
def create_rains(rain_setting,screen,rains):
    rain = RainDrop(rain_setting,screen)
    number_rain_lines = get_number_rain_line(rain_setting,rain)
    number_rain_rows = get_number_rain_row(rain_setting,rain)
    for number_rain_row in range(number_rain_rows):
        for number_rain_line in range(number_rain_lines):
            create_rain(rain_setting,screen,number_rain_line,number_rain_row,rains)

def update_screen(rain_setting,screen,rains):
    # 填充屏幕，并且把雨滴的编组按照上面函数赋予的坐标绘制到屏幕
    screen.fill(rain_setting.bg_color)
    rains.draw(screen)
    pygame.display.flip()

def update_rain(rains,rain_setting,screen):
    for rain in rains.sprites():
        if rain.check_edge():
            # 让触底的雨滴重新出现在屏幕的最上方的关键就在于把这个触底的雨滴给移除编组，
            # 因为哪个触底的雨滴已经被写出到了编组里，应该已经无法被修改，
            # 因此上面出现的雨滴需要是新的雨滴对象
            new_rain = RainDrop(rain_setting,screen)
            new_rain.rect.x = rain.rect.x
            new_rain.rect.y = rain.rect.height
            rains.remove(rain)
            rains.add(new_rain)
    rains.update()

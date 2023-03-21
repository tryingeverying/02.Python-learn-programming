import sys
import pygame
from function_13_3_star import Star

# 正常退出程序
def check_keydown_events():
    """响应键被按下的情况"""
    for event in pygame.event.get():
        if event.type == pygame.K_q:
            sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

# 计算屏幕上一行能够放置多少个星星
def get_number_star_line(star_setting, star):
    available_space_line = star_setting.screen_width - 2 * star.rect.width
    number_star_line = int(available_space_line / (2 * star.rect.width))
    return number_star_line

# 计算屏幕上可以放置多少行的星星
def get_number_row(star_setting, star):
    available_space_row = star_setting.screen_height - 2 * star.rect.height
    number_row = int(available_space_row / (2 * star.rect.height))
    return number_row 

# 生成单个星星
def create_star(star_setting,screen,star_number,star_row,stars):
    star = Star(star_setting,screen)
    # 在生成星星的时候星星的类需要重新初始化，否则每次在生成新对象的时候上个对象都会被全局变量覆写
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2 * star_width * star_number
    star.y = star_height + 2 * star_height * star_row
    star.rect.x = star.x 
    star.rect.y = star.y 
    # 把生成具有上述坐标的星星存入星星的编组中
    stars.add(star)

# 创建一群的星星
def create_stars(star_setting,screen,stars):
    star = Star(star_setting,screen)
    star_numbers = get_number_star_line(star_setting, star)
    star_rows = get_number_row(star_setting, star)
    for star_row in range(star_rows):
        for star_number in range(star_numbers):
            create_star(star_setting,screen,star_number,star_row,stars)

# 把生成的星星群绘制到屏幕上
def update_screen(star_setting,screen,stars):
    screen.fill(star_setting.bg_color)
    stars.draw(screen)
    pygame.display.flip()




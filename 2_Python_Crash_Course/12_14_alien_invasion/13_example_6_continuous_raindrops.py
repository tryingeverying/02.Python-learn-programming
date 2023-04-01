"""13-4 连绵细雨 ：修改为完成练习13-3而编写的代码，
使得一行雨滴消失在屏幕底端后，屏幕顶端又出现一行新雨滴，并开始往下落。"""

import pygame, sys
from function_12_1_setting import Settings
from pygame.sprite import Sprite, Group

class RainDrop(Sprite):
    """一个关于雨滴的类"""
    def __init__(self, rain_setting,screen) -> None:
        super(RainDrop, self).__init__()
        self.screen = screen
        self.rain_setting = rain_setting
        # 导入图片，并且通过get_rect方法获取其外接矩形
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\raindrop.bmp")
        self.rect = self.image.get_rect()
        # 图片出现的初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 将图片的初始位置设定为可以是float
        self.x = float(self.rect.x )
        self.y = float(self.rect.y )

    def blitme(self):
        # 将图片绘制到屏幕上
        self.screen.blit(self.image,self.rect)

    def check_edge(self):
        # 检测雨滴是否到达屏幕的底部
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.bottom:
            return True

    def update(self):
        # 雨滴往下掉落
        self.y += self.rain_setting.rain_speed_factor
        self.rect.y = self.y

def rain_drop():
    """初始化屏幕"""
    pygame.init()
    rain_setting = Settings()
    screen = pygame.display.set_mode((rain_setting.screen_width,
                                      rain_setting.screen_height))
    pygame.display.set_caption("雨滴掉落")

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
    def create_rains(rain_setting,screen):
        rain = RainDrop(rain_setting,screen)
        number_rain_lines = get_number_rain_line(rain_setting,rain)
        number_rain_rows = get_number_rain_row(rain_setting,rain)
        for number_rain_row in range(number_rain_rows):
            for number_rain_line in range(number_rain_lines):
                create_rain(rain_setting,screen,number_rain_line,number_rain_row,rains)

    def update_screen(rain_setting,screen):
        # 填充屏幕，并且把雨滴的编组按照上面函数赋予的坐标绘制到屏幕
        screen.fill(rain_setting.bg_color)
        rains.draw(screen)
        pygame.display.flip()

    def update_rain(rains):
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
    
    # 创建一个雨滴的编组
    rains = Group()
    create_rains(rain_setting,screen)
    while True:
        # 监控键盘的情况
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_q]:
                sys.exit()
        update_rain(rains)
        update_screen(rain_setting,screen)

if  __name__ == "__main__":
    rain_drop()


















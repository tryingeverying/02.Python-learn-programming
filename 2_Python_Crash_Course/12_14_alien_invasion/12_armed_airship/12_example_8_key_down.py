"""12-4 按键 ：创建一个程序，显示一个空屏幕。
在事件循环中，每当检测到pygame.KEYDOWN 事件时都打印属性event.key 。
运行这个程序，并按各种键，看看Pygame如何响应。"""

import pygame
import sys

def key_down():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("按键测试")
    bg_color = (199,237,204)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.key)
        
        screen.fill(bg_color)
        pygame.display.flip()


key_down()    











import sys
import pygame

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()  # 初始化背景设置，让Pygame能够正确地工作
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("外星人入侵")

    # 设置背景色
    bg_color = (230,230,230)

    # 开始主游戏循环
    while True:

        # 监视键盘和鼠标的操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕 
        screen.fill(bg_color)   
        # 用背景色填充屏幕；这个方法只接受一个实参：一种颜色。

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
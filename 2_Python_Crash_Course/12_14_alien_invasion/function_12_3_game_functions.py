import sys
import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向右移动飞船
                ship.moving_left = True    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # 如果有键被松开且松开的键为右键则移动标记换为False
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # 如果有键被松开且松开的键为右键则移动标记换为False
                ship.moving_ = False


def update_screen(ai_setting,screen,ship):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()






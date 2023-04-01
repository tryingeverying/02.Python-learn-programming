import sys
import pygame

def check_keydown_events(event,rocket):
    """响应键被按下的情况"""
    if event.key == pygame.K_RIGHT:
    # 向右移动火箭
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
    # 向右移动火箭
        rocket.moving_left = True 
    elif event.key == pygame.K_UP:
    # 向右移动火箭
        rocket.moving_up = True 
    elif event.key == pygame.K_DOWN:
    # 向右移动火箭
        rocket.moving_down = True 
    
def check_keyup_events(event,rocket):
    """响应键被松开且松开的键为方向键的情况"""
    if event.key == pygame.K_RIGHT:
    # 如果有键被松开且松开的键为右键则移动标记换为False
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
    # 如果有键被松开且松开的键为右键则移动标记换为False
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
    # 如果有键被松开且松开的键为上键则移动标记换为False
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
    # 如果有键被松开且松开的键为下键则移动标记换为False
        rocket.moving_down = False

def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rocket)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)


def update_screen(ai_setting,screen,rocket):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    rocket.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()






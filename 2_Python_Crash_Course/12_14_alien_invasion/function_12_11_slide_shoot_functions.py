import sys
import pygame
from function_12_10_slide_bullet import Bullet

def check_keydown_events(event,ai_settings,screen,rocket,bullets):
    """响应键被按下的情况"""
    if event.key == pygame.K_UP:
    # 向右移动火箭
        rocket.moving_up = True 
    elif event.key == pygame.K_DOWN:
    # 向右移动火箭
        rocket.moving_down = True 
    elif event.key == pygame.K_RIGHT:
    # 向右移动火箭
        rocket.moving_right = True 
    elif event.key == pygame.K_LEFT:
    # 向右移动火箭
        rocket.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,rocket,bullets)

def fire_bullet(ai_settings,screen,rocket,bullets):
    """如果还没有达到限制就发射一颗子弹"""
    # 创建一个子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,rocket)
        bullets.add(new_bullet)

def check_keyup_events(event,rocket):
    """响应键被松开且松开的键为方向键的情况"""
    if event.key == pygame.K_UP:
    # 如果有键被松开且松开的键为上键则移动标记换为False
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
    # 如果有键被松开且松开的键为下键则移动标记换为False
        rocket.moving_down = False
    elif event.key == pygame.K_RIGHT:
    # 向右移动火箭
        rocket.moving_right = False 
    elif event.key == pygame.K_LEFT:
    # 向右移动火箭
        rocket.moving_left = False 

def check_events(ai_settings,screen,rocket,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,rocket,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)

def update_screen(ai_setting,screen,rocket,bullets):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 子弹移动
    bullets.update()

    # 删除子弹横坐标值大于窗口右边界的子弹
    for bullet in bullets.copy():
        if bullet.rect.right > bullet.screen_rect.right:
            bullets.remove(bullet)




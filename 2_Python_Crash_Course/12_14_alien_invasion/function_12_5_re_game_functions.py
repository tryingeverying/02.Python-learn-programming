import sys
import pygame
from function_12_8_bullet import Bullet

"""重构game_function函数 使其模块化"""
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应键被按下的情况"""
    if event.key == pygame.K_RIGHT:
    # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制就发射一颗子弹"""
    # 创建一个子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def check_keyup_events(event,ship):
    """响应键被松开且松开的键为左右键的情况"""
    if event.key == pygame.K_RIGHT:
    # 如果有键被松开且松开的键为右键则移动标记换为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
    # 如果有键被松开且松开的键为右键则移动标记换为False
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_setting,screen,ship,bullets):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    # 在飞船和外星人后面重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 子弹移动
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)







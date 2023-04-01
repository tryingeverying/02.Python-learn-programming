import pygame
import sys
from function_13_8_GoldToad import GoldToad
from function_13_9_Coppers import Coppers
from random import randint

def check_event(goldtoad):
    """监控键盘的操作"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,goldtoad)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,goldtoad)

def check_keydown_events(event,goldtoad):
    if event.key == pygame.K_RIGHT:
        goldtoad.moving_right = True
    elif event.key == pygame.K_LEFT:
        goldtoad.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,goldtoad):
    if event.key == pygame.K_RIGHT:
        goldtoad.moving_right = False
    elif event.key == pygame.K_LEFT:
        goldtoad.moving_left = False

def create_goldtoad(cc_settings,screen,goldtoads):
    """创建一个金蟾"""
    goldtoad = GoldToad(cc_settings,screen)
    screen_rect = screen.get_rect()
    goldtoad.rect.centerx = screen_rect.centerx
    goldtoad.rect.bottom = screen_rect.bottom
    goldtoads.add(goldtoad)

def create_copper(cc_settings,coppers, screen):
    """创建一个铜钱"""
    copper = Coppers(cc_settings,screen)
    screen_rect = screen.get_rect()
    start_x_min = int(copper.rect.width / 2)
    start_x_max = int(screen_rect.right - copper.rect.width / 2)
    copper.rect.centerx = randint(start_x_min,start_x_max)
    
    # 把生成的铜钱加入到编组中
    coppers.add(copper)

def check_copper_goldtoad_collisions(cc_settings,goldtoads, coppers, screen):
    """检测铜钱和金蟾的撞击情况"""
    collisions = pygame.sprite.groupcollide(goldtoads, coppers, False, True)
    
    # 金蟾和铜钱发生碰撞后铜钱消失，而金蟾依旧存在
    if len(coppers) == 0:
        create_copper(cc_settings,coppers, screen)
    for copper in coppers.copy():
        if copper.check_bottom():
            coppers.remove(copper)
            # create_copper(coppers, screen)
            # print(len(coppers))
            # 如果触底判断为true，则把这个铜钱的对象移除编组，
            # 此时编组的len为0，触发上面的判断生成一个新的铜钱对象
            # 因为编组的值可以为任意个，若把remove行给注释掉，
            # 而取消下面两行的注视就可以发现如果不移除copper，
            # coppers编组的长度会不断累加，所以不能在for循环中创建铜钱对象，
            # 否则会出现很多个铜钱

def update_screen(screen,cc_settings,goldtoads,coppers):
    """刷新屏幕"""
    screen.fill(cc_settings.bg_color)
    goldtoads.draw(screen)
    coppers.draw(screen)

    # 把参数绘制到屏幕上
    pygame.display.flip()

def update_location(cc_settings,goldtoads,coppers,screen):
    coppers.update()
    for goldtoad in goldtoads:
        check_event(goldtoad)
        goldtoad.update()
        # 为了实现碰撞的判断，我把goldtoad类继承了sprite从而实现的碰撞判断的功能
        # 但是此时的goldtoads已经不是单个类，而是一个编组，
        # check_event函数只能实现对于单个对象的控制，
        # 因此之前的代码无法实现通过键盘操作goldtoad的移动，
        # 为了实现移动功能只能在goldtoads编组中取出单独的goldtoad对象，
        # 使之调用check_event从而实现对goldtoad的操控
    check_copper_goldtoad_collisions(cc_settings,goldtoads, coppers, screen)
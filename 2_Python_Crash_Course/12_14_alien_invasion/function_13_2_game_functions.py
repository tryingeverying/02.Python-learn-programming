import sys
import pygame
from function_12_8_bullet import Bullet
from function_13_1_alien import Alien

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


def update_screen(ai_setting,screen,ship,bullets,aliens):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    # 在飞船和外星人后面重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 对编组调用draw() 时，Pygame自动绘制编组的每个元素，
    # 绘制位置由元素的属性rect 决定。
    # 在这里，aliens.draw(screen) 在屏幕上绘制编组中的每个外星人。    
    aliens.draw(screen)
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 子弹移动
    bullets.update()
    # 检测是否有子弹击中了外星人
    # 如果又被击中的就删除相应的子弹和外星人
    # 两个实参 True 告诉Pygame删除发生碰撞的子弹和外星人。
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，
    # 可将第一个布尔实参设置为False ，并让第二个布尔实参为True 。
    # 这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。
    if len(aliens) == 0:
        bullets.empty()
        # 上面调用了pygame.sprite.groupcollide方法，
        # 也就意味着碰撞判定为true的子弹和外星人会被删除，
        # 此时如果aliens的编组的字节为空也就意味着外星人的编组已经清空了，
        # 对应的子弹的编组也要清空，以便重新按下space时出现的子弹是新的。
        # 但是即便是没有也不会有太大的影响
        create_fleet(ai_settings, screen, ship, aliens)
    # # 删除已经消失的子弹
    # for bullet in bullets.copy():
    #     if bullet.rect.bottom <= 0:
    #         bullets.remove(bullet)
    # 如果上面的pygame.sprite.groupcollide的bulle赋值为False，
    # 即bullet在与alien的碰撞后不消失则需要调用上面的代码删除已经消失在屏幕上的bullet。
    # 从而使得屏幕的子弹可以重新出现
    
def get_number_aliens_x(ai_settings,alien_width):
    """计算屏幕的可用空间能够容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕上可以容纳多少行的外星人"""
    available_space_y = (ai_settings.screen_height - 
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并且将其放在当前行"""
    # 创建一个外星人，并且计算一行可以容纳多少外星人
    # 外星人间距是外星人的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建多行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edge(ai_settings, aliens):
    """有外星人达到边缘是采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """外星人向下移动，并且改变外星人的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edge(ai_settings, aliens)
    aliens.update()    




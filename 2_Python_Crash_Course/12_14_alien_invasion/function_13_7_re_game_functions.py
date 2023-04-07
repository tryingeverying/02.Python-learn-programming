import sys
import pygame
from time import sleep
from function_12_8_bullet import Bullet
from function_13_1_alien import Alien


"""重构game_function函数 使其模块化"""

def check_events(ai_settings,screen,ship,aliens,bullets,sb,stats,play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,aliens,bullets,stats,)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,ship,aliens,bullets,sb,stats,
                    play_button,mouse_x,mouse_y)

def check_keydown_events(event,ai_settings,screen,ship,aliens,bullets,stats,):
    """响应键被按下的情况"""
    if event.key == pygame.K_RIGHT:
    # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
    # 向右移动飞船
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_F2:
        start_game(ai_settings,screen,ship,aliens,bullets,stats,)

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

    # 重构update_bullets
def update_bullets(ai_settings,screen,ship,aliens,bullets,stats,sb):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 子弹移动
    bullets.update()
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens,stats,sb)
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
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

def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets,):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edge(ai_settings, aliens)
    aliens.update()    

    # 检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb, screen, ship, aliens, bullets)
        
    # 监控外星人是否达到屏幕底部
    check_aliens_bottom(ai_settings,stats,sb, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens,stats,sb):
    """检测外星人和子弹的碰撞情况"""
    # 检测是否有子弹击中了外星人
    # 如果又被击中的就删除相应的子弹和外星人
    # 两个实参 True 告诉Pygame删除发生碰撞的子弹和外星人。
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # 要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，
    # 可将第一个布尔实参设置为False ，并让第二个布尔实参为True 。
    # 这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。
    if collisions :
        # 在check_bullet_alien_collisions() 中，
        # 与外星人碰撞的子弹都是字典collisions 中的一个键；
        # 而与每颗子弹相关的值都是一个列表，
        # 其中包含该子弹撞到的外星人
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        bullets.empty()
        # 上面调用了pygame.sprite.groupcollide方法，
        # 也就意味着碰撞判定为true的子弹和外星人会被删除，
        # 此时如果aliens的编组的字节为空也就意味着外星人的编组已经清空了，
        # 对应的子弹的编组也要清空，以便重新按下space时出现的子弹是新的。
        # 但是即便是没有也不会有太大的影响

        # 调用设置中的加速设置，提升游戏难度
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_aliens_bottom(ai_settings,stats,sb, screen, ship, aliens, bullets):
    """检查是否有外星人达到屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            # 外星人达到屏幕底部，当作飞船被击中处理
            ship_hit(ai_settings,stats,sb, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings,stats,sb, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 飞船的生命值减一
        stats.ships_left -= 1
        # 更新计分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一个新的外星人群，并且把飞船放到屏幕的底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂定游戏
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    
# 14-1 按P开始新游戏 ：鉴于游戏《外星人入侵》使用键盘来控制飞船，
# 最好让玩家也能够通过按键来开始游戏。请添加让玩家在按P时开始游戏的代码。
# 也许这样做会有所帮助：将check_play_button() 的一些代码提取出来，
# 放到一个名为start_game() 的函数中，
# 并在check_play_button()和check_keydown_events() 中调用这个函数。

def start_game(ai_settings,screen,ship,aliens,bullets,stats,):
    stats.reset_stats()
    # 重新游戏统计信息
    stats.game_active = True

    # 清空外星人的列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一个新的外星人群，并且让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_play_button(ai_settings,screen,ship,aliens,bullets,sb,stats,
                    play_button,mouse_x,mouse_y):
    """如果玩家点击play按钮开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    # collidepoint() 检查鼠标单击位置是否在Play按钮的rect内
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        ai_settings.initialize_dynamic_settings()
        # 重新游戏统计信息
        stats.game_active = True

        # 重置计分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人的列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一个新的外星人群，并且让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 通过向set_visible() 传递False ，
        # 让Pygame在光标位于游戏窗口内时将其隐藏起来

def check_high_score(stats,sb):
    """"检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_screen(ai_setting,screen,ship,bullets,aliens,sb,stats,play_button):
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
    # 显示得分
    sb.show_score()

    # 如果一开始游戏处于非激活状态，就绘制"开始"按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()


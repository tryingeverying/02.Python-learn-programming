# 14-2 射击练习 ：创建一个矩形，它在屏幕右边缘以固定的速度上下移动。
# 然后，在屏幕左边缘创建一艘飞船，玩家可上下移动该飞船，并射击前述矩形目标。
# 添加一个用于开始游戏的Play按钮，在玩家三次未击中目标时结束游戏，
# 并重新显示Play按钮，让玩家能够通过单击该按钮来重新开始游戏。

import pygame
import sys
from function_12_1_setting import Settings
from pygame.sprite import Sprite,Group
from random import randint
from time import sleep


class Rocket():
    """一个关于火箭的类"""
    
    def __init__(self,sp_settings,screen) -> None:
        """初始化火箭并设置初始位置"""
        self.screen = screen
        self.ai_settings = sp_settings

        # 加载飞船图像并获取其外接矩阵
        self.image = pygame.image.load(r'2_Python_Crash_Course\12_14_alien_invasion\images\rocket_slide.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.x = self.screen_rect.x
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.x = float(self.rect.x)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭的位置"""
        # 更新飞船的center值，而非rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.rocket_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.rocket_speed_factor
        
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor
        
        
        # 根据self.center更新rect对象
        self.rect.x = self.x
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制火箭"""
        # 把图片image绘制到screen上的rect的位置
        self.screen.blit(self.image,self.rect)

class Bullets(Sprite):
    """对火箭发射的子弹进行管理"""
    def __init__(self,sp_setting,screen,rocket) -> None:
        """在火箭所处的位置处创建一个子弹"""
        super(Bullets,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,sp_setting.bullet_height,
                                sp_setting.bullet_width)
        self.rect.right = rocket.rect.right
        self.rect.centery = rocket.rect.centery
        # 把飞船的中心的横坐标和飞船顶部的纵坐标赋值给子弹的中心和顶部

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.right)

        self.color = sp_setting.bullet_color
        self.speed_factor = sp_setting.bullet_speed_factor
    
    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数点
        self.x += self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.right = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

class Rect(Sprite):
    """一个关于被射击矩形的类"""
    def __init__(self,sp_settings,screen) -> None:
        """在火箭所处的位置处创建一个子弹"""
        super(Rect,self).__init__()
        self.screen = screen
        self.sp_settings = sp_settings
        self.screen_rect = self.screen.get_rect()
        # 在(0,0)处创建一个表示被射击的矩形，在设置rect的位置
        self.rect = pygame.Rect(0,0,50,80)
        self.rect.right = self.screen_rect.right
        self.rect.bottom = self.screen_rect.y
        
        
        self.y = float(self.rect.bottom)

        self.color = (255,255,0)
        self.speed_factor = 0.5

    def check_edges(self):
        """如果矩形位于屏幕边缘，返回true"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
        
    def update(self):
        """上下移动矩形"""
        # 更新表示子弹位置的小数点
        self.y += self.speed_factor * self.sp_settings.fleet_direction
        # 更新表示子弹的rect的位置
        self.rect.y = self.y


    def draw_rect(self):
        """在屏幕上绘制矩形"""
        pygame.draw.rect(self.screen,self.color,self.rect)

class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, sp_settings) -> None:
        """初始化数据"""
        self.sp_settings = sp_settings
        self.reset_stats()
        # 使游戏一开始处于非运行状态
        self.game_active = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.rects_left = self.sp_settings.error_times

class Button():
    """关于按钮的类"""
    def __init__(self,sp_settings,screen,msg) -> None:
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸以及其他属性
        self.width ,self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象，并且使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True,
                            self.text_color,self.button_color)
        # font.render() 将存储在msg 中的文本转换为图像，
        # 然后将该图像存储在msg_image 中
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


def run_game():

    def check_keydown_events(event,sp_settings,screen,rocket,bullets,):
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
            fire_bullet(sp_settings,screen,rocket,bullets)
        

    def fire_bullet(ai_settings,screen,rocket,bullets):
        """如果还没有达到限制就发射一颗子弹"""
        # 创建一个子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullets(ai_settings,screen,rocket)
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
    
    def check_events(sp_settings,screen,rocket,rects,bullets,stats,play_button):        
        # 监控键盘和鼠标的动作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,sp_settings,screen,rocket,bullets,)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,rocket)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(sp_settings,screen,rocket,rects,bullets,stats,play_button,mouse_x,mouse_y)

    def update_bullets(bullets):
        """更新子弹的位置，并删除已经消失的子弹"""
        # 子弹移动
        bullets.update()

        # 删除子弹横坐标值大于窗口右边界的子弹
        for bullet in bullets.copy():
            if bullet.rect.right > bullet.screen_rect.right:
                bullets.remove(bullet)

    def create_rect(sp_settings, screen, rects):
        """创建一个被射击的矩形，centery随机"""
        # 创建一个外星人，并且计算一行可以容纳多少外星人
        # 外星人间距是外星人的宽度
        rect = Rect(sp_settings, screen)
        screen_rect = screen.get_rect()
      
        rect.rect.right = screen_rect.right
        rect.y = randint(0,screen_rect.bottom)
        # 下面这个把生成的随机值赋值给纵坐标才是实现对初始位置的随机化
        rect.rect.bottom = rect.y 
        

        rects.add(rect)

    def check_rect_edge(sp_settings, rects):
        """有外星人达到边缘是采取措施"""
        for rect in rects.sprites():
            if rect.check_edges():
                change_rect_direction(sp_settings)
                break

    def change_rect_direction(sp_settings):
        """改变矩形的方向"""
        sp_settings.fleet_direction *= -1
    
    def check_bullet_alien_collisions(sp_settings, screen, bullets, rects,):
        """检测矩形和子弹的碰撞情况"""
        collisions = pygame.sprite.groupcollide(bullets, rects, False, True)
        if len(rects) == 0:
            bullets.empty()
            create_rect(sp_settings, screen, rects)
            sleep(0.05)

    def update_rects(sp_settings,rects,):

        for rect in rects.sprites():
            # 绘制矩形
            rect.draw_rect()
            """更新矩形的位置"""
            check_rect_edge(sp_settings, rects)
            rects.update()  
    
    def check_play_button(sp_settings,screen,rocket,rects,bullets,stats,play_button,mouse_x,mouse_y):
        """如果玩家点击play按钮开始新游戏"""
        button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
        # collidepoint() 检查鼠标单击位置是否在Play按钮的rect内
        if button_clicked and not stats.game_active:
            stats.reset_stats()
            # 重新游戏统计信息
            stats.game_active = True

            # 清空外星人的列表和子弹列表
            rects.empty()
            bullets.empty()

            # 创建一个新的外星人群，并且让飞船居中
            create_rect(sp_settings, screen, rects)

            # 隐藏光标
            pygame.mouse.set_visible(False)
            # 通过向set_visible() 传递False ，
            # 让Pygame在光标位于游戏窗口内时将其隐藏起来

    def update_screen(ai_setting,screen,rocket,bullets,rects):
        """更新屏幕上的图像，并且切换到新屏幕"""
        # 每次循环都重绘屏幕
        screen.fill(ai_setting.bg_color)
        # 绘制子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        rocket.blitme()

        for rect in rects.sprites():  
            rect.draw_rect()

        check_bullet_alien_collisions(sp_settings, screen, bullets, rects,)
        # 如果游戏处于非激活状态绘制按钮
        if not stats.game_active:
            play_button.draw_button()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    # 初始化游戏界面
    pygame.init()
    sp_settings = Settings()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("射击练习")

    rocket = Rocket(sp_settings,screen)
    bullets = Group()
    rects = Group()

    # 创建游戏开始按钮
    play_button = Button(sp_settings,screen, "Play !")
    # 创建一个用于存储游戏信息的实例
    stats = GameStats(sp_settings)
    # 创建一个待射击的矩形对象
    create_rect(sp_settings, screen, rects)

    while True:

        check_events(sp_settings,screen,rocket,rects,bullets,stats,play_button)
        if stats.game_active:
            # 火箭的上下移动
            rocket.update()
            # 控制子弹
            update_bullets(bullets)
            update_rects(sp_settings,rects)

        # 绘制屏幕
        update_screen(sp_settings,screen,rocket,bullets,rects)
    


if __name__ == "__main__":
    run_game()


















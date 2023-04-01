"""13-5 抓球 ：创建一个游戏，在屏幕底端放置一个玩家可左右移动的角色。
让一个球出现在屏幕顶端，且水平位置是随机的，并让这个球以固定的速度往下落。
如果角色与球发生碰撞（表示将球抓住了），就让球消失。
每当角色抓住球或球因抵达屏幕底端而消失后，都创建一个新球。"""
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from function_12_1_setting import Settings
import sys
from random import randint

class GoldToad(Sprite):
    """定义一个关于金蟾的类"""
    def __init__(self, cc_settings, screen) -> None:
        super(GoldToad,self).__init__()
        self.cc_settings = cc_settings
        self.screen = screen

        # 加载金蟾的图像以及图像信息
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\goldtoad.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 确定金蟾的初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.x = self.screen_rect.centerx
        # self.rect.y= self.screen_rect.bottom
        # pygame里的xy值指的是图上的左上角，
        # 如上面那种写法图片的左上角的横坐标是屏幕的中心，
        # 图像左上角的纵坐标是屏幕的底部,
        # 也就是说图像左上角的坐标是屏幕底边的中点，
        # 图像整个都在屏幕下面了，屏幕上肯定没有图像显示了
        # 精确化金蟾的横坐标
        self.x = float(self.rect.centerx)
        # 移动判断符
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """使得金蟾可以左右移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.cc_settings.toad_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.cc_settings.toad_speed_factor
        self.rect.centerx = self.x

    def blitme(self):
        """将金蝉的图像绘制到屏幕上"""
        self.screen.blit(self.image,self.rect)


class Coppers(Sprite):
    """一个关于铜钱的类"""
    def __init__(self, cc_settings, screen) -> None:
        """初始化参数"""
        super(Coppers,self).__init__()
        self.cc_settings = cc_settings
        self.screen = screen

        # 加载铜钱图像和图像参数
        self.image = pygame.image.load(r"2_Python_Crash_Course\12_14_alien_invasion\images\coppers.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化铜钱的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """把铜钱绘制到屏幕上"""
        self.screen.blit(self.image,self.rect)

    def check_bottom(self):
        """检测铜钱是否触底"""
        if self.rect.bottom > self.screen_rect.bottom:
            return True
    
    def update(self):
        """让铜钱下落"""
        self.y += self.cc_settings.copper_drop_speed
        self.rect.y = self.y

def run_game():
    # 初始化pygame,设置以及屏幕
    pygame.init()
    cc_settings = Settings()
    screen = pygame.display.set_mode(
        (cc_settings.screen_width,cc_settings.screen_height)
    )
    pygame.display.set_caption("吞财金蟾")

    goldtoads = Group()
    coppers = Group()

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

    def create_copper(coppers, screen):
        """创建一个铜钱"""
        copper = Coppers(cc_settings,screen)
        screen_rect = screen.get_rect()
        start_x_min = int(copper.rect.width / 2)
        start_x_max = int(screen_rect.right - copper.rect.width / 2)
        copper.rect.centerx = randint(start_x_min,start_x_max)
        
        # 把生成的铜钱加入到编组中
        coppers.add(copper)
    
    def check_copper_goldtoad_collisions(goldtoads, coppers, screen):
        """检测铜钱和金蟾的撞击情况"""
        collisions = pygame.sprite.groupcollide(goldtoads, coppers, False, True)
        
        # 金蟾和铜钱发生碰撞后铜钱消失，而金蟾依旧存在
        if len(coppers) == 0:
            create_copper(coppers, screen)
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
    
    def update_location(goldtoads,coppers):
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
        check_copper_goldtoad_collisions(goldtoads,coppers,screen)

    create_goldtoad(cc_settings,screen,goldtoads)
    create_copper(coppers, screen)
    
    while True:
        
        update_screen(screen,cc_settings,goldtoads,coppers)
        update_location(goldtoads,coppers)


if __name__ == "__main__":
    run_game()












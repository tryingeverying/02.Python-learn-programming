"""13-2 更逼真的星星 ：为让星星的分布更逼真，可随机地放置星星。
本书前面说过，可像下面这样来生成随机数：
```python
from random import randint
random_number = randint(-10,10)
```
上述代码返回一个-10和10之间的随机整数。
在为完成练习13-1而编写的程序中，随机地调整每颗星星的位置。
"""
import pygame,sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint
from function_12_1_setting import Settings

class Star(Sprite):
    """一个关于星星的类"""
    def __init__(self,star_setting,screen):
        """初始化屏幕和设置类"""
        super(Star, self).__init__()
        self.screen = screen
        self.star_setting = star_setting
        # 导入图片并且获取图片的外接矩形
        self.image = pygame.image.load(r"02.Python-learn-programming\2_Python_Crash_Course\12_14_alien_invasion\images\star.bmp")
        self.rect = self.image.get_rect()
        # 将图片的初始位置放置在屏幕上
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 图片的坐标值可以是小数
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # 将星星图片绘制到屏幕的rect位置
        self.screen.blit(self.image, self.rect)

def star_screen():
    """初始化屏幕数据"""
    pygame.init()
    star_setting = Settings()
    screen = pygame.display.set_mode((star_setting.screen_width,
                                     star_setting.screen_height))
    pygame.display.set_caption("星星铺满屏幕")

    # 创建一个星星的编组
    stars = Group()

    # 计算屏幕上一行能够放置多少个星星
    def get_number_star_line(star_setting, star):
        available_space_line = star_setting.screen_width - 2 * star.rect.width
        number_star_line = int(available_space_line / (2 * star.rect.width))
        return number_star_line
    
    # 计算屏幕上可以放置多少行的星星
    def get_number_row(star_setting, star):
        available_space_row = star_setting.screen_height - 2 * star.rect.height
        number_row = int(available_space_row / (2 * star.rect.height))
        return number_row 
    
    # 生成单个星星
    def create_star(star_number,star_row,stars):
        star = Star(star_setting,screen)
        # 在生成星星的时候星星的类需要重新初始化，否则每次在生成新对象的时候上个对象都会被全局变量覆写
        star_width = star.rect.width
        star_height = star.rect.height
        star.x = randint(0,150) + 2 * randint(0,150) * star_number
        star.y = randint(0,100) + 2 * randint(0,100) * star_row
        star.rect.x = star.x 
        star.rect.y = star.y 
        # 把生成具有上述坐标的星星存入星星的编组中
        stars.add(star)

    # 创建一群的星星
    def create_stars(star_setting,stars):
        # 初始化一个星星对象
        star = Star(star_setting,screen)
        star_numbers = get_number_star_line(star_setting, star)
        star_rows = get_number_row(star_setting, star)
        for star_row in range(star_rows):
            for star_number in range(star_numbers):
                create_star(star_number,star_row,stars)

    # 把生成的星星群绘制到屏幕上
    def update_screen(star_setting,stars):
        screen.fill((250,250,250))
        stars.draw(screen)
        pygame.display.flip()


    create_stars(star_setting,stars)

    while True:
        # 监视键盘和鼠标的操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 让最近绘制的屏幕可见
        update_screen(star_setting,stars)


star_screen()











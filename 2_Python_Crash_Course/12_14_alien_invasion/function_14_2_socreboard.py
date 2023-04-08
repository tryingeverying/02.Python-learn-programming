import pygame.font
from pygame.sprite import Group

from function_12_2_ship import Ship

class Scoreboard():
    """显示得分情况的看板"""

    def __init__(self,ai_settings,screen,stats) -> None:
        """初始化分数看板的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings =ai_settings
        self.stats = stats

        # 设置显示得分情况时显示的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        # 绘制分数等级图像
        self.prep_image()

# 14-5 重构 ：找出执行了多项任务的函数和方法，
# 对它们进行重构，以让代码高效而有序。
    def prep_image(self):
        # 准备得分数据的图像
        self.prep_score()
        # 记录最高得分
        self.prep_high_score()
        # 显示等级
        self.prep_level()
        # 显示飞船图标
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅图像"""
        rounded_score = int(round(self.stats.score, -1))
        # 函数round() 通常让小数精确到小数点后多少位，
        # 其中小数位数是由第二个实参指定的。
        # 然而，如果将第二个实参指定为负数，
        # round() 将圆整到最近的10、100、1000等整数倍。
        score_str = "{:,}".format(rounded_score)
        # 它让Python将数值转换为字符串时在其中插入逗号，
        # 例如，输出1,000,000 而不是1000000
        self.score_image = self.font.render("Score: " + score_str,True,
                                self.text_color,self.ai_settings.bg_color)

        # 将得分情况放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """将最高分转换为图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("High Score: "+ high_score_str,True,
                                    self.text_color,self.ai_settings.bg_color)

        # 将最高得分绘制到屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """将最高分转换为图像"""
        self.level_image = self.font.render("Level: " + str(self.stats.level),
                                    True,self.text_color,self.ai_settings.bg_color)

        # 将最高得分绘制到屏幕顶部中央
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number  * (ship.rect.width + 10)
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        














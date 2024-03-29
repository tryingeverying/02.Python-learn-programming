class Settings():
    """存储 外星人入侵 的所有设置的类"""

    def __init__(self) -> None:
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (199,237,204)

        # 飞船的设置
        
        self.ship_limit = 3
        
        # 火箭的设置
        self.rocket_speed_factor = 2.5

        # 子弹设置
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # 游戏节奏设置
        # 移动速度的提升倍数
        self.speedup_scale = 1.1
        # 外星人分值的提升速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
        # 雨滴的设置
        self.rain_speed_factor = 1
        
        # 金蟾和铜钱的设置
        self.toad_speed_factor = 1.5
        self.copper_drop_speed = 0.6
        self.error_times = 2

        # 矩形的移动速度
        self.error_times = 3

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.rect_speed_factor = 0.5

        # fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.rect_speed_factor *= self.speedup_scale
        # 随着速度的提升，得分上升
        self.alien_points = int(self.alien_points * self.score_scale)









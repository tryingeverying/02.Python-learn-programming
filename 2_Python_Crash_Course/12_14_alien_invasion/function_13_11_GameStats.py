
class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, ai_settings) -> None:
        """初始化数据"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 使游戏一开始处于非运行状态
        self.game_active = False
        # 最高分数
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1







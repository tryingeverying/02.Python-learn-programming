
class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, cc_settings) -> None:
        """初始化数据"""
        self.cc_settings = cc_settings
        self.reset_stats()
        # 游戏运行判断符
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.chances = self.cc_settings.error_times







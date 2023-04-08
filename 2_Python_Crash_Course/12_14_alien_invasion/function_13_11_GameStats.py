
class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, ai_settings) -> None:
        """初始化数据"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 使游戏一开始处于非运行状态
        self.game_active = False
        # 最高分数
        # 14-4 历史最高分 ：每当玩家关闭并重新开始游戏《外星人入侵》时，
        # 最高分都将被重置。请修复这个问题，调用sys.exit() 前将最高分写入文件，
        # 并当在GameStats 中初始化最高分时从文件中读取它。
        filename = r"2_Python_Crash_Course\12_14_alien_invasion\high_score_record.txt"
        with open(filename) as f_b:
            hs = f_b.read()
        self.high_score = int(float(hs))

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1







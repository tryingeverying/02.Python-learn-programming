from random import randint

class Die():
    """一个关于骰子的类"""
    def __init__(self, num_sides = 6) -> None:
        """骰子的面数"""
        self.num_sides = num_sides

    def roll(self):
        # 返回一个介于1到骰子面数之间的随机数
        return randint(1,self.num_sides)











# 15-5 重构 ：方法fill_walk() 很长。请新建一个名为get_step() 的方法，
# 用于确定每次漫步的距离和方向，并计算这次漫步将如何移动。
# 然后，在fill_walk() 中调用get_step()两次
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points = 5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 随机漫步的起始点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着该方向前进的距离
            x_step = self.get_step()

            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        # 决定前进方向以及沿着该方向前进的距离
        dirdection = choice([-1,1])
        distance = choice([0,1,2,3,4,])
        step = dirdection * distance

        return step












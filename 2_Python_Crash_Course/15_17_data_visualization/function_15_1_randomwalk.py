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
            x_dirdection = choice([-1,1])
            x_distance = choice([0,1,2,3,4,])
            x_step = x_dirdection * x_distance

            y_dirdection = choice([-1,1])
            y_distance = choice([0,1,2,3,4,])
            y_step = y_dirdection * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)












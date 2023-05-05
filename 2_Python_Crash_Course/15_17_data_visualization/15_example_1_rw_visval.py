import matplotlib.pyplot as plt

from function_15_2_re_randomwalk import RandomWalk

# 只要程序是激活状态就不断模拟随机漫步
while True:
    
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(dpi=128,figsize=(10,6))
    # 函数figure() 用于指定图表的宽度、高度、分辨率和背景色。
    # 形参figsize 指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。
    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # 上面的操作会造成数据不显示，需将坐标轴赋值给一个对象，对该对象调用坐标轴方法。
    # 且该操作需要在绘制图像之前，即在plt.scatter前
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c = point_numbers,
                cmap=plt.cm.Blues, edgecolors="none", s = 1)

    # 突出起点和终点
    plt.scatter(0,0,c="green",edgecolors="none",s=80)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="yellow",edgecolors="none",s=80)

    # 绘制图像
    plt.show()

    keep_running = input("开启另一个随机漫步？(y/n):")
    if keep_running == "n":
        break

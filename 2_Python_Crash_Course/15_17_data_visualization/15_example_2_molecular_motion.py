import matplotlib.pyplot as plt

from function_15_2_re_randomwalk import RandomWalk

# 15-3 分子运动 ：修改rw_visual.py，将其中的plt.scatter()替换为plt.plot()。
# 为模拟花粉在水滴表面的运动路径，向plt.plot() 传递rw.x_values 和rw.y_values ，
# 并指定实参值linewidth 。使用5000个点而不是50 000个点。

while True:
    
    mm = RandomWalk(5000)
    mm.fill_walk()
    # 设置窗口和分辨率
    plt.figure(dpi=128,figsize=(10,6))

    # 隐藏坐标轴
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)



    point_numbers = list(range(mm.num_points))
    plt.plot(mm.x_values,mm.y_values,linewidth = 3,)

    # # 绘制图像
    plt.show()

    keep_running = input("开启另一个随机漫步？(y/n):")
    if keep_running == "n":
        break
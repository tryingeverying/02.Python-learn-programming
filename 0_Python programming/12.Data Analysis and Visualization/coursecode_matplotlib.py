

import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # 创建一个包含一个坐标系的图表
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # 分别为 x y 轴赋值来画出一系列的点，默认用折线图来展示

plt.show() # 需要调用 plt.show() 才会显示出界面
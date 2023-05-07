# 15-6 自动生成标签 ：请修改die.py和dice_visual.py，
# 将用来设置hist.x_labels 值的列表替换为一个自动生成这种列表的循环。
# 如果你熟悉列表解析，尝试将die_visual.py和dice_visual.py中的其他for 循环也替换为列表解析。

import pygal
from function_15_3_die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 对得到的数据进行可视化分析
hist = pygal.Bar()

hist.title = "结果分析"
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12',
#                 '13','14','15','16',]
# hist.x_labels = [str(x) for x in range(1,max_result + 1)]
hist.x_labels =map(str,range(2,max_result + 1) )
# map方法可以实现和上面哪个列表推导式一样的目标
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('D6+D10', frequencies)
hist.render_to_file(r"2_Python_Crash_Course\15_17_data_visualization\img\difference_dice_visual.svg")






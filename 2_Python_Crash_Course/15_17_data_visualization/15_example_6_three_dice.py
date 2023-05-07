# 15-8 同时掷三个骰子 ：如果你同时掷三个D6骰子，可能得到的最小点数为3，
# 而最大点数为18。请通过可视化展示同时掷三个D6骰子的结果。
import pygal
from function_15_3_die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 对得到的数据进行可视化分析
hist = pygal.Bar()

hist.title = "结果分析"
hist.x_labels = map(str,range(3,max_result + 1))
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('D6+D10', frequencies)
hist.render_to_file(r"2_Python_Crash_Course\15_17_data_visualization\img\three_dice_visual.svg")






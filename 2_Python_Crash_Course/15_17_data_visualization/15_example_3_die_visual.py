import pygal
from function_15_3_die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 对得到的数据进行可视化分析
hist = pygal.Bar()

hist.title = "结果分析"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12',]
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add('D6', frequencies)
hist.render_to_file(r"2_Python_Crash_Course\15_17_data_visualization\img\dice_visual.svg")






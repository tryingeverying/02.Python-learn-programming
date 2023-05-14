import csv
from matplotlib import pyplot as plt

filename = r"2_Python_Crash_Course\15_17_data_visualization\res\sitka_weather_07-2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    next_row = next(reader)
    # 函数next() ，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。
    # print(header_row,"\n",next_row)
    
    # for index, column_header in enumerate(header_row):
    # # enumerate枚举方法实现给遍历对象加上索引值
    #     print(index,column_header)

    highs = []
    for row in reader:
        high = int(row[4])
        highs.append(high)

    print(highs)

    # 使用上面的数据绘制图形
    fig = plt.figure(dpi=128, figsize=(8,5))
    plt.plot(highs, c = "red")

    # 设置图形的格式
    plt.title('The max temperature')
    plt.xlabel("", fontsize = 16)
    plt.ylabel("temperature(F) :", fontsize = 16)
    plt.tick_params(axis='both', which = "major", labelsize = 16)

    plt.show()







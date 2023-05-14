# 处理数据存在缺失的情况
import  csv
from datetime import datetime

from matplotlib import pyplot as plt

# 读取文件中的日期,最高气温和最低气温
filename = r"2_Python_Crash_Course\15_17_data_visualization\res\death_valley_2021_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2],"%Y-%m-%d")
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            # 应对数据丢失的情况
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 利用上面的数据绘制图像
fig = plt.figure(dpi = 128, figsize=(10,6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5) 
# 填充两条线的中间区域
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
plt.title("daily high temperature, 2014 \n Death Valley, CA ", fontsize = 24)
plt.xlabel('', fontsize = 16)

fig.autofmt_xdate()
plt.ylabel("temperature (F)", fontsize = 16)
plt.tick_params(axis="both", which = "major", labelsize = 16)


plt.show()


import csv
from datetime import datetime

from matplotlib import pyplot as plt

#get temperature and date information
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#调用了一次next得到文件的第一行

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
       
        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

    #draw picture
    fig = plt.figure(dpi=128, figsize=(8,5))#窗口设置
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()#绘制斜的日期标签
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)#设置刻度的样式

    plt.show()

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

#给坐标轴加标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#axis是显示哪个坐标轴，which可以设为major,minor,both，为主刻度，次刻度或者都显示
#labelsize是刻度的字号
plt.tick_params(axis='both', which='major', labelsize=14)


#每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

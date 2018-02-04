import matplotlib.pyplot as plt 

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

#s表示点的大小
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.axis([0,5000,0,1.3e11])

plt.show()

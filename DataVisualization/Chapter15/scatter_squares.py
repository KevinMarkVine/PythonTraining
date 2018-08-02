#绘制散点图
import matplotlib.pyplot as plt

'''
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', s=20)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Valus", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

#设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()

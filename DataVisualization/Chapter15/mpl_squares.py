import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6, 7]
squares = [1, 4, 9, 16, 25, 36, 49]

#linewidth是线条粗细
plt.plot(input_values, squares,linewidth=5)

#设置图表标题，给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
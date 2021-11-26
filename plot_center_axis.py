import numpy as np
import matplotlib.pyplot as plt

"""
this code 主要实现将坐标原点移动图像中心
"""
# print(np.pi)
theta = np.linspace(0, 2*np.pi, 1000)

# 求幂次
polar_coordinate = np.power(np.sin(theta), 4)

# 对应元素相乘
x = polar_coordinate * np.cos(theta)
y = polar_coordinate * np.sin(theta)
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("x")
ax.set_ylabel("y")
# 去掉上边和右边
ax.spines["right"].set_color('None')
ax.spines["top"].set_color('None')
# 设置x 和 y 的坐标轴 好像没什么用 哈哈
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置坐标轴的刻度间隔
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_xticks([-0.3, -0.15, 0, 0.15, 0.3])
# 移动x 和 y的坐标轴
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.plot(x, y, color='g')
plt.show()

# print(polar_coordinate)
# print(theta)

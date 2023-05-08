# 绘制散点图，主要用到plt.scatter（）这个函数。
# x,y是必填参数；
# c(颜色：b--blue, c--cyan,g--green,k--black,m--magenta,r--red,w--white,y--yellow)；
# s：控制点的大小，默认为20；
# marker：指定散点图点的形状，默认为圆形；
# alpha：指定对象的透明度；
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
s = (30 * np.random.rand(50))**2
plt.scatter(x, y,s, c=colors, alpha=0.5)

plt.show()
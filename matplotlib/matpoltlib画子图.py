import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,200) # 从0到10之间等距产生200个值

# 使用子图
# 如果需要将多张子图展示在一起，可以使用 subplot() 实现。即在调用 plot()函数之前需要先调用 subplot() 函数。
# 该函数的第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活跃区域。
ax1 = plt.subplot(2, 2, 1)
plt.plot(x,np.sin(x), 'k')

ax2 = plt.subplot(2, 2, 2, sharey=ax1) # ax2 与 ax1 共享y轴
plt.plot(x, np.cos(x), 'g')

ax3 = plt.subplot(2, 2, 3)
plt.plot(x,x, 'r')

ax4 = plt.subplot(2, 2, 4, sharey=ax3) # ax4 与 ax3 共享y轴
plt.plot(x, 2*x, 'y')

# 保存图片,必须写在show之前
plt.savefig("imgs/子图.png")
plt.show()


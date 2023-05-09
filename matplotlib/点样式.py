import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 5)

plt.plot(y,'o') # 圆形
plt.plot(y+1,'D') # 菱形

# 指定marker时，会画出线段：
plt.plot(y+2,marker = '^') # 三角形
plt.plot(y+3,marker = 'p') # 五角形

plt.savefig("imgs/点样式.png")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 5)

# 1.八种内件颜色缩写：
# b:blue
# g:green
# r:red
# c:cyan
# m:magenta
# y:yellow
# k:black
# w:white

# 不写线形,默认为实线
plt.plot(y, color='b') # 蓝色

# 灰色程度
plt.plot(y+1, color='0.5') # 程度为0.5

# 十六进制颜色表示
plt.plot(y+2,color='#FFEC8B')

# RGB表示,此时注意要将R，G，B每个值除以255，使其属于0~1之间
plt.plot(y+3,color=(1,0.4,0.6))

plt.savefig("imgs/颜色.png")
plt.show()
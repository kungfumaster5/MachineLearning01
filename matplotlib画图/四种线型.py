import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 5)

# 四种线型
plt.plot(y, '-')  # 实线,默认实线
plt.plot(y + 1, '--')  # 虚线
plt.plot(y + 2, '-.')  # 点划线
plt.plot(y + 3, ':')  # 点线

plt.savefig("imgs/四种线型.png")
plt.show()

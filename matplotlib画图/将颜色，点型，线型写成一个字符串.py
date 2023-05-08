import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1, 5)

plt.plot(y,'gx:')
plt.plot(y+1,'mo--')
plt.plot(y+2,'bp-')
plt.plot(y+3,'rD-.')

plt.savefig("imgs/组合样式.png")
plt.show()
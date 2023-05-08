import matplotlib.pyplot as plt
plt.title("标题")
# 解决中文标题乱码问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(6, 3))
plt.plot(6, 3)
plt.plot(3, 3 * 2)
plt.show()
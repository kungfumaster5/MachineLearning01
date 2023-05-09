import matplotlib.pyplot as plt
import numpy as np
# Matplotlib是整个包，pyplot是Matplotlib中的一个模块
# matplotlib是可视化的表达，那么在图形的绘制中肯定会涉及一些数据处理。
# pandas和numpy则是python中最好用的两个数据分析库，使用它们，能够解决超过90%的数据分析问题。

# matplotlib的图的构成元素：
# 坐标轴(axis)、坐标轴名称(axis label)、坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、标题(title)......

# 设置标题
plt.title("标题")
# 解决中文标题乱码问题
plt.rcParams['font.sans-serif']=['SimHei']
# 设置x轴坐标轴范围
plt.xlim(0,6)
# 设置y轴坐标轴范围
plt.ylim((-3, 3))
# 设置x轴标签
plt.xlabel('X轴')
# 设置y轴标签
plt.ylabel('Y轴')

# 如果需要将坐标轴的数字设为负数，也可能出现乱码的情况
plt.rcParams['axes.unicode_minus']=False

# 创建数据
x=np.linspace(0,10,200) # 从0到10之间等距产生200个值
y1 = np.sin(x)
y2 = np.cos(x)

# 设置图例
plt.plot(x, y1, linestyle=':', color='r', label="sin") # 第一个label
plt.plot(x, y2, label="cos") # 第二个labrel
plt.legend(loc='best') # 图列位置，可选best，center等

# 添加注释:有时候我们需要对特定的点进行标注，我们可以使用 plt.annotate 函数来实现
# s: 注释信息内容
# xy:箭头点所在的坐标位置
# xytext:注释内容的坐标位置
# arrowprops：设置指向箭头的参数
plt.annotate(text='(3,sin(3))',xy=(3,np.sin(3)),xytext=(4,1), arrowprops=dict(arrowstyle='-|>'))

plt.show()
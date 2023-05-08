# Numpy 中 arange() 主要是用于生成数组，具体用法如下:
# 1.语法：
# numpy.arange(start, stop, step, dtype = None)
# 在给定间隔内返回均匀间隔的值，
# 值在半开区间 [开始，停止)内生成（换句话说，包括开始但不包括停止的区间）,返回的是 ndarray 。

# 2.参数：
# start —— 开始位置，数字，可选项，默认起始值为0
# stop —— 停止位置，数字
# step —— 步长，数字，可选项， 默认步长为1，如果指定了step，则还必须给出start。
# dtype —— 输出数组的类型。 如果未给出dtype，则从其他输入参数推断数据类型。

# 3.返回：
# arange：ndarray
# 均匀间隔值的数组，结果的长度为ceil((stop - start)/step)
# 注意：对于浮点参数（参数为浮点），由于浮点溢出，此规则可能导致最后一个元素>=stop。因此要特别注意

# 4.实例
from numpy import *  # 引入numpy

A = arange(5)  # 默认起始值为0，默认步长为1
print(A)  # 结果 [0 1 2 3 4] 结果不包含结束项
print(type(A))  # 结果 <class 'numpy.ndarray'>

A = arange(1, 5)  # 起点为1，步长默认为1
print(A)  # 结果 [1 2 3 4]

A = arange(1, 5, 2)  # 步长默认为2
print(A)  # 结果 [1 3]

A = arange(1, 5.2, 0.6)  # 浮点数参数，结果就不一定完全符合了
print(A)  # 结果 [1.  1.6 2.2 2.8 3.4 4.  4.6 5.2]

import numpy as np
import matplotlib.pyplot as plt
import scipy
import sklearn

# 1.sklearn是scikit-learn的简称，是一个基于Python的第三方模块。sklearn库集成了一些常用的机器学习方法，
# 在进行机器学习任务时并不需要实现算法，只需要简单的调用sklearn库中提供的模块就能完成大多数的机器学习任务。
# sklearn库是在Numpy、Scipy和matplotlib的基础上开发而成的，因此在介绍sklearn的安装前，需要先安装这些依赖库。
#
# 2.Numpy(Numerical Python的缩写)是一个开源的Python科学计算库。在Python中虽然提供了list容器和array模块，
# 但这些结构并不适合于进行数值计算，因此需要借助于Numpy库创建常用的数据结构（如：多维数组，矩阵等）以及进行常用的科学计算（如：矩阵运算）。
#
# 3.Scipy库是sklearn库的基础，它是基于Numpy的一个集成了多种数学算法和函数的Python模块。它的不同子模块有不同的应用，如：积分、插值、优化和信号处理等。
#
# 4.matplotlib是基于Numpy的一套Python工具包，它提供了大量的数据绘图工具，主要用于绘制一些统计图形，将大量的数据转换成更加容易被接受的图表。
# (注意要先安装numpy，再安装matplotlib库)



# 通过终端pip安装
# pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple

# 测试numpy是否安装成功，创建arrar数组
array = np.array([i for i in range(10)])
print(array) # [0 1 2 3 4 5 6 7 8 9]

# 查看模块库安装位置
print(np.__file__) # E:\env\python-3.9.2\lib\site-packages\numpy\__init__.py


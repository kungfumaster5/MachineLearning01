# ctrl+alt+L 格式化代码

# sklearn库的共分为6大部分，分别用于完成分类任务、回归任务、聚类任务、降维任务、及模型选择以数据的预处理。


# 1.波士顿房价数据集: 波士顿房价数据集包含506组数据，每条数据包含房屋以及房屋周围的详细信息。用于回归问题
# 加载相关数据集
from sklearn.datasets import load_boston
# 其重要参数为：return_X_y:表示是否返回target（即价格)，默认为False，只返回data(即属性)。

boston = load_boston()
print(boston.data.shape) # (506,13)

data,target = load_boston(return_X_y=True)
print(target.shape) # (506)

# 注意：波士顿房价数据集已经不可用!
# ImportError:
# `load_boston` has been removed from scikit-learn since version 1.2.
#
# The Boston housing prices dataset has an ethical problem: as
# investigated in [1], the authors of this dataset engineered a
# non-invertible variable "B" assuming that racial self-segregation had a
# positive impact on house prices [2]. Furthermore the goal of the
# research that led to the creation of this dataset was to study the
# impact of air quality but it did not give adequate demonstration of the
# validity of this assumption.
#
# The scikit-learn maintainers therefore strongly discourage the use of
# this dataset unless the purpose of the code is to study and educate
# about ethical issues in data science and machine learning.



# 2.鸢尾花（鸳鸯）数据集：鸢尾花数据集采集的是鸢尾花的测量数据以及其所属的类别。用于分类问题
# 加载相关数据集
from sklearn.datasets import load_iris

# 其参数有：return_X_y:若为True，则以（data, target）形式返回数据；默认为False，表示以字典形式返回数据全部信息（包括data和target）。
# 转成人话就是返回一个参数还是两个参数
iris = load_iris()
print(iris.data.shape)  # (150, 4)
print(iris.target.shape)  # (150,)

data, target = load_iris(return_X_y=True)
print(data.shape, target.shape)  # (150, 4) (150,)
print(list(iris.target_names))  # ['setosa', 'versicolor', 'virginica']


# 3.手写数字数据集:
# 手写数字数据集包括1797个0-9的手写数字数据，每个数字由8*8大小的矩阵构成，矩阵中值的范围是0-16，代表颜色的深度。
# 加载相关数据集
from sklearn.datasets import load_digits

# 其参数包括：
# return_X_y:若为True，则以（data, target）形式返回数据；默认为False，表示以字典形式返回数据全部信息（包括data和target）
# n_class：表示返回数据的类别数，如：n_class=5,则返回0到4的数据样本。
digits = load_digits()
print(digits.data.shape, digits.target.shape)  # (1797, 64) (1797,)
print(digits.images.shape)  # (1797, 8, 8)

import matplotlib.pyplot as plt
# 绘制矩阵图
plt.matshow(digits.images[0]) # digits.images[0]为数据集的第一张图
plt.show()

# print(digits.images[0])
# [[ 0.  0.  5. 13.  9.  1.  0.  0.]
#  [ 0.  0. 13. 15. 10. 15.  5.  0.]
#  [ 0.  3. 15.  2.  0. 11.  8.  0.]
#  [ 0.  4. 12.  0.  0.  8.  8.  0.]
#  [ 0.  5.  8.  0.  0.  9.  8.  0.]
#  [ 0.  4. 11.  0.  1. 12.  7.  0.]
#  [ 0.  2. 14.  5. 10. 12.  0.  0.]
#  [ 0.  0.  6. 13. 10.  0.  0.  0.]]

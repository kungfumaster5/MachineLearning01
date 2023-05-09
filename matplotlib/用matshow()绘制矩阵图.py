import matplotlib.pyplot as plt
import numpy as np
# 设置0-100的10*10的矩阵
matA = np.arange(0, 100).reshape(10, 10)
plt.matshow(matA, cmap=plt.cm.Reds)#这里设置颜色为红色，也可以设置其他颜色
# 设置颜色为蓝色 plt.matshow(mat, cmap=plt.cm.Blues)
# 设置颜色为灰色 plt.matshow(mat, cmap=plt.cm.gray)
plt.title("matrix A")
plt.show()


# 随机设置矩阵 B
matB=np.array([[4,3,2,4],[5,4,7,8],[9,16,11,5],[13,3,4,16],[6,18,1,20]])
# 不同的数值大小红色的深度是不一样的，数值越大红色越深
plt.matshow(matB, cmap=plt.cm.Reds)
# 主图旁一个长条状的小图，能够辅助表示主图中 colormap 的颜色组成和颜色与数值的对应关系
plt.colorbar()
plt.title("matrix B")
plt.show()

# 用plt.colorbar绘制矩阵图
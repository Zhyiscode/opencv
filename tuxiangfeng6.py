import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 应用Sobel边缘检测
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度的幅度
magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# 将梯度幅度归一化到范围[0, 255]
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

# 转换为uint8以便显示
magnitude = np.uint8(magnitude)

# 对幅度进行阈值处理，得到二值边缘图像
_, edges = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)

# 显示原始图像和Sobel边缘检测结果
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原始图像')
plt.subplot(1, 3, 2), plt.imshow(magnitude, cmap='gray'), plt.title('Sobel梯度幅度')
plt.subplot(1, 3, 3), plt.imshow(edges, cmap='gray'), plt.title('Sobel边缘检测')
plt.show()

'''基于边缘的分割： 使用边缘检测算法（如Canny、Sobel）来找到图像中的边缘，从而分割物体。'''
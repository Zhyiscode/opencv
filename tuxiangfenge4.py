import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 使用Canny边缘检测进行分割
edges = cv2.Canny(img, 50, 150)

# 显示原始图像和边缘检测后的图像
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Edge-based Segmentation')
plt.show()
'''基于边缘的分割： 使用边缘检测算法（如Canny、Sobel）来找到图像中的边缘，从而分割物体。'''
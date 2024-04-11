import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 使用拉普拉斯算子进行图像锐化
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 显示原始图像和锐化后的图像
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray'), plt.title('Sharpened Image')
plt.show()
'''拉普拉斯算子进行图像锐化'''
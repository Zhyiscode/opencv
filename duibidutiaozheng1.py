import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 线性拉伸对比度调整
alpha = 1.2  # 调整因子
beta = 20    # 偏移量

adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# 显示原始图像和调整后的图像
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(adjusted_img, cmap='gray'), plt.title('Adjusted Image')
plt.show()
'''线性拉伸对比度调整'''
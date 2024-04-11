import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 定义锐化卷积核
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# 使用卷积进行图像锐化
sharpened_img = cv2.filter2D(img, -1, kernel)

# 显示原始图像和锐化后的图像
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(sharpened_img, cmap='gray'), plt.title('Sharpened Image')
plt.show()

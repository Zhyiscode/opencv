'''分水岭算法'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用Sobel算子计算梯度
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度幅值和方向
gradient_mag = np.sqrt(grad_x**2 + grad_y**2)
gradient_dir = np.arctan2(grad_y, grad_x)

# 应用阈值和二值化
_, gradient_mag_binary = cv2.threshold(gradient_mag, 50, 255, cv2.THRESH_BINARY)
gradient_mag_binary = gradient_mag_binary.astype(np.uint8)

# 膨胀操作
kernel = np.ones((3, 3), np.uint8)
sure_bg = cv2.dilate(gradient_mag_binary, kernel, iterations=2)

# 显示原始图像和分水岭分割后的图像
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(sure_bg, cmap='gray'), plt.title('Watershed Segmentation')
plt.show()

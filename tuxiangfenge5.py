import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 使用分水岭算法进行区域分割
_, markers = cv2.connectedComponents(img)

# 显示原始图像和分水岭分割后的图像
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(markers, cmap='jet'), plt.title('Region-based Segmentation')
plt.show()
'''基于区域的分割： 将图像分成具有相似属性的区域，例如区域生长算法、分水岭算法'''
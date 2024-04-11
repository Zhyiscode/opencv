import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 使用固定阈值进行分割
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# 显示原始图像和分割后的图像
'''plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')'''

plt.subplot(), plt.imshow(binary_img, cmap='gray'), plt.title('Threshold Segmentation')
plt.savefig( 'D:\\pycharmyunxing\\venv\\exam_01.png')
plt.show()
'''阈值分割'''
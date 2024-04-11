import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape图像为二维数组
pixels = img_rgb.reshape((-1, 3))

# 将图像分成K个类别
k = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
_, labels, centers = cv2.kmeans(pixels.astype(np.float32), k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 将每个像素标记为其所属的类别
segmented_img = centers[labels.flatten().astype(int)].reshape(img_rgb.shape)

# 显示原始图像和K均值聚类分割后的图像
plt.subplot(1, 2, 1), plt.imshow(img_rgb), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(segmented_img.astype(np.uint8)), plt.title('K-Means Segmentation')
plt.show()
'''K均值聚类'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_gabor_filter(image, ksize, sigma, theta, lambd, gamma, psi):
    # 获取图像的宽度和高度
    rows, cols = image.shape

    # 创建Gabor滤波器的响应矩阵
    kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, psi)

    # 对图像应用Gabor滤波器
    filtered_image = cv2.filter2D(image, cv2.CV_8UC3, kernel)

    return filtered_image

# 读取图像
image = cv2.imread('D:\\pycharmyunxing\\venv\\image1.png',0)

# 设置Gabor滤波器的参数
ksize = 30
sigma = 9.0
theta = np.pi / 2
lambd = 10.0
gamma = 0.8
psi = 0.2

# 应用Gabor滤波器
filtered_image = apply_gabor_filter(image, ksize, sigma, theta, lambd, gamma, psi)

# 显示原始图像和滤波后的图像
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)), plt.title('Filtered Image')
plt.xticks([]), plt.yticks([])
plt.show()
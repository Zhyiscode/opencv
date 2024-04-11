'''import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("D:\\pycharmyunxing\\venv\\qiaoba.png",0)
for i in range(2000):
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

blur_1 = cv2.GaussianBlur(img,(5,5),0)\
# 高斯滤波

blur_2 = cv2.medianBlur(img,5)
# 中值滤波

plt.subplot(1,3,1),plt.imshow(img,'gray')
plt.subplot(1,3,2),plt.imshow(blur_1,'gray')
plt.subplot(1,3,3),plt.imshow(blur_2,'gray')
plt.show()'''

'''对图形像进行平滑1处理，两种方式高斯滤波和中值滤波和均值滤波和双边滤波'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# 在图像上添加噪声
for i in range(2000):
    temp_x = np.random.randint(0, img.shape[0])
    temp_y = np.random.randint(0, img.shape[1])
    img[temp_x][temp_y] = 255

# 高斯滤波
blur_gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
blur_median = cv2.medianBlur(img, 5)

# 均值滤波
blur_mean = cv2.blur(img, (5, 5))

# 双边滤波
blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 显示原始图像和各种平滑处理后的图像
plt.subplot(2, 3, 1), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.subplot(2, 3, 2), plt.imshow(blur_gaussian, 'gray'), plt.title('Gaussian Blur')
plt.subplot(2, 3, 3), plt.imshow(blur_median, 'gray'), plt.title('Median Blur')
plt.subplot(2, 3, 4), plt.imshow(blur_mean, 'gray'), plt.title('Mean Blur')
plt.subplot(2, 3, 5), plt.imshow(blur_bilateral, 'gray'), plt.title('Bilateral Blur')

plt.show()

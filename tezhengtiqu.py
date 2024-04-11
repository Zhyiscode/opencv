'''import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("D:\\pycharmyunxing\\venv\\qiaoba.jpg",0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gxay')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gxay')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gxay')
plt.title('solel x'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gxay')
plt.title('solel y'),plt.xticks([]),plt.yticks([])
plt.show()'''

'''使用Laplacian算子进行边缘检测。
使用Sobel算子进行水平和垂直方向的边缘检测'''


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('sobel x'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('sobel y'), plt.xticks([]), plt.yticks([])

plt.show()

'''Canny边缘检测和Scharr算子'''


'''import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)

# Canny边缘检测
edges_canny = cv2.Canny(img, 40, 80)

# Scharr算子
scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
edges_scharr = np.sqrt(scharrx**2 + scharry**2)

# 显示原始图像、Canny边缘检测结果和Scharr算子边缘检测结果
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(edges_scharr, cmap='gray')
plt.title('Scharr Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()'''
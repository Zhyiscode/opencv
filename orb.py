'''import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("D:\\pycharmyunxing\\venv\\yan1.png", 0)
img2 = cv2.imread("D:\\pycharmyunxing\\venv\\yan2.png", 0)
orb = cv2.ORB_create()
kp1 , des1 = orb.detectAndCompute(img1, None)
kp2 , des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)
plt.imshow(img3),plt.show()'''

'''
# 使用的是ORB特征检测器，和BFMatcher (暴力匹配器)匹配两幅图像的关键点
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取图像
img1 = cv2.imread("D:\\pycharmyunxing\\venv\\yan1.png", 0)
img2 = cv2.imread("D:\\pycharmyunxing\\venv\\yan2.png", 0)

# 创建ORB检测器
orb = cv2.ORB_create()

# 寻找关键点和描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 创建BFMatcher (暴力匹配器)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 使用BFMatcher匹配关键点
matches = bf.match(des1, des2)

# 将匹配点按照距离升序排列
matches = sorted(matches, key=lambda x: x.distance)

# 绘制前10个匹配点
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# 显示图像
plt.imshow(img3)
plt.show()'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# 读取图像
img1 = cv2.imread("D:\\pycharmyunxing\\venv\\yan1.png", 0)
img2 = cv2.imread("D:\\pycharmyunxing\\venv\\yan2.png", 0)

# Initiate ORB detector
orb = cv2.ORB_create()

# 寻找关键点和描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 创建BFMatcher (暴力匹配器)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 使用BFMatcher匹配关键点
matches = bf.match(des1, des2)

# 将匹配点按照距离升序排列
matches = sorted(matches, key=lambda x: x.distance)

# 获取匹配点的坐标
pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# 计算透视变换矩阵
M, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)

# 应用透视变换
result = cv2.warpPerspective(img1, M, (img1.shape[1] + img2.shape[1], max(img1.shape[0], img2.shape[0])))

# 将第二张图叠加到结果图像上
result[0:img2.shape[0], 0:img2.shape[1]] = img2

# 显示结果
plt.imshow(result, cmap='gray')
plt.show()





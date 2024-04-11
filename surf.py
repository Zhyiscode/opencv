'''import cv2
import numpy as np

img = cv2.imread("D:\\pycharmyunxing\\venv\\qiaoba.png",0)
surf = cv2.SIFT_create(400)

surf.setContrastThreshold(50000)

kp, des = surf.detectAndCompute(img,None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
cv2.imshow("surf",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()'''
# surf 在opencv中为找不到surf了，搜索结果是可能在opencv库中已经废弃

import cv2

img = cv2.imread("D:\\pycharmyunxing\\venv\\image2.png", 0)

# 使用SIFT算法，并设置一些参数
sift = cv2.SIFT_create(contrastThreshold=0.04, edgeThreshold=10)

# 检测关键点和计算描述符
kp, des = sift.detectAndCompute(img, None)

# 绘制关键点
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
cv2.imshow("SIFT", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

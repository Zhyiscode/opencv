import cv2
from matplotlib import pyplot as plt

img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)
res = cv2.equalizeHist(img)
clahe = cv2.createCLAHE(clipLimit=2,tileGridSize=(10,10))
cl1 = clahe.apply(img)
plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(res,'gray')
plt.subplot(133),plt.imshow(cl1,'gray')
plt.show()
# 限制对比度的自适应直方图均衡化
import cv2
import numpy as np

# 读取图像
img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")

# 转换图像颜色空间为LAB
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# 分割LAB通道
l_channel, a_channel, b_channel = cv2.split(lab_img)

# 计算平均亮度
avg_l = np.mean(l_channel)

# 计算亮度比例因子
scale_factor = 128 / avg_l

# 调整亮度通道
adjusted_l_channel = cv2.multiply(l_channel, scale_factor)

# 合并通道
adjusted_lab_img = cv2.merge([adjusted_l_channel, a_channel, b_channel])

# 转换回BGR颜色空间
result_img = cv2.cvtColor(adjusted_lab_img, cv2.COLOR_LAB2BGR)

# 显示原始图像和调整后的图像
cv2.imshow('Original Image', img)
cv2.imshow('White Balance Adjusted Image', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

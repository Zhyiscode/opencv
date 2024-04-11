'''灰度-彩色变换法'''
import cv2
import numpy as np

def apply_color_map(gray_image, colormap=cv2.COLORMAP_JET):
    # 将灰度图像应用颜色映射
    color_image = cv2.applyColorMap(gray_image, colormap)
    return color_image

# 读取灰度图像
gray_image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", cv2.IMREAD_GRAYSCALE)

# 应用颜色映射
pseudocolor_image = apply_color_map(gray_image, cv2.COLORMAP_JET)

# 显示原始灰度图像和伪彩色增强后的图像
cv2.imshow('Original Gray Image', gray_image)
cv2.imshow('Pseudocolor Enhanced Image', pseudocolor_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

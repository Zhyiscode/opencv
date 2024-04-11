'''密度分层法'''
import cv2
import numpy as np

def density_slicing_pseudocolor(image, thresholds, colors):
    # 创建一个全零矩阵，用于存储伪彩色图像
    pseudocolor_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    # 对每个密度范围进行颜色映射
    for i in range(len(thresholds) + 1):
        if i == 0:
            pseudocolor_image[(image <= thresholds[i])] = colors[i]
        elif i == len(thresholds):
            pseudocolor_image[(image > thresholds[i - 1])] = colors[i]
        else:
            pseudocolor_image[(image > thresholds[i - 1]) & (image <= thresholds[i])] = colors[i]

    return pseudocolor_image

# 读取灰度图像
gray_image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", cv2.IMREAD_GRAYSCALE)

# 定义密度分层的阈值和颜色
thresholds = [50, 100, 150, 200]  # 定义阈值
colors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]  # 定义颜色

# 进行密度分层伪彩色增强
enhanced_image = density_slicing_pseudocolor(gray_image, thresholds, colors)

# 显示原始灰度图像和增强后的伪彩色图像
cv2.imshow('Original Gray Image', gray_image)
cv2.imshow('Pseudocolor Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

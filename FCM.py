import numpy as np
import cv2
import skfuzzy as fuzz

# 读取图像
image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")

# 将图像转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 将图像像素值归一化到 [0, 1] 区间
gray_image = gray_image / 255.0

# 将灰度图像转换为一维数组
data = gray_image.reshape((-1, 1))

# 设置模糊聚类的参数
num_clusters = 5  # 聚类数
m = 2  # 模糊参数
error = 0.005  # 收敛误差
max_iter = 1000  # 最大迭代次数

# 使用 FCM 算法进行模糊聚类
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    data.T, num_clusters, m, error, max_iter, seed=0)

# 获取最大隶属度的索引作为像素类别
segmented_image = np.argmax(u, axis=0)

# 将一维数组转换回图像形状
segmented_image = segmented_image.reshape(gray_image.shape)

# 将像素类别映射为颜色（可选）
segmented_image = (segmented_image * (255 / (num_clusters - 1))).astype(np.uint8)

# 显示原始图像和分割后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

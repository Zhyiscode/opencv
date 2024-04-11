import cv2
import numpy as np
from matplotlib import pyplot as plt
# 读取图像
image = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Gamma校正
gamma = 1.5
gamma_corrected_image = np.power(image / 255.0, gamma) * 255.0
gamma_corrected_image = gamma_corrected_image.astype(np.uint8)

cv2.imshow('image',image)
cv2.imshow('gamma_corrected_image',gamma_corrected_image)
cv2.waitKey(0)

plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(gamma_corrected_image, cmap='gray'), plt.title('Adjusted Image')
plt.show()

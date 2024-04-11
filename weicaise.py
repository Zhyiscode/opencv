# import cv2
# import numpy as np
#
# def retinex_transform(image, sigma=300):
#     # 将图像转换为浮点数类型
#     image = image.astype(np.float32)
#
#     # 对数域中的Retinex算法
#     retinex = np.log10(image) - np.log10(cv2.GaussianBlur(image, (0, 0), sigma))
#
#     # 将结果缩放到0-255范围
#     retinex = (retinex - np.min(retinex)) / (np.max(retinex) - np.min(retinex)) * 255
#     retinex = retinex.astype(np.uint8)
#
#     return retinex
#
# # 读取图像
# original_image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")
#
# # 转换图像为灰度图像
# gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#
# # 对灰度图像应用Retinex变换
# retinex_image = retinex_transform(gray_image)
#
# # 显示原始图像和Retinex变换后的图像
# cv2.imshow('Original Image', original_image)
# cv2.imshow('Retinex Transformed Image', retinex_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
#
# def gamma_correction(image, gamma=1.0):
#     # 应用Gamma校正
#     inv_gamma = 1.0 / gamma
#     table = np.array([((i / 255.0) ** inv_gamma) * 255
#                       for i in np.arange(0, 256)]).astype("uint8")
#     return cv2.LUT(image, table)
#
# def gamma_clahe(image, gamma=1.0, clip_limit=2.0, tile_size=(8, 8)):
#     # 应用Gamma校正
#     gamma_corrected = gamma_correction(image, gamma)
#
#     # 应用CLAHE直方图均衡化
#     clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)
#     clahe_image = clahe.apply(gamma_corrected)
#
#     # 将CLAHE图像和Gamma校正图像混合
#     blended = cv2.addWeighted(gamma_corrected, 0.5, clahe_image, 0.5, 0)
#
#     return blended
#
# # 读取图像
# original_image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png",cv2.IMREAD_GRAYSCALE)
#
# # 对图像应用混合“γ-CLAHE”算法
# blended_image = gamma_clahe(original_image, gamma=1.5, clip_limit=3.0, tile_size=(8, 8))
#
# # 显示原始图像和处理后的图像
# cv2.imshow('Original Image', original_image)
# cv2.imshow('Gamma-CLAHE Enhanced Image', blended_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from pycontour import Contourlet

def contourlet_msrcr_enhancement(image):
    # 进行Contourlet变换
    contourlet = Contourlet(image)
    subbands = contourlet.transform()

    # 对每个Contourlet子带应用MSRCR算法
    enhanced_subbands = []
    for subband in subbands:
        enhanced_subband = apply_msrcr(subband)  # 应用MSRCR算法
        enhanced_subbands.append(enhanced_subband)

    # 将处理后的Contourlet子带进行逆变换
    enhanced_image = contourlet.inverse_transform(enhanced_subbands)

    return enhanced_image

def apply_msrcr(subband):
    # 在每个子带上应用MSRCR算法，实现颜色恢复和对比度增强
    # 这里可以使用基于引导滤波的MSRCR算法进行处理
    # 返回处理后的子带
    return enhanced_subband

# 读取输入图像
input_image = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png")

# 对输入图像应用Contourlet变换和MSRCR算法
enhanced_image = contourlet_msrcr_enhancement(input_image)

# 显示增强后的图像
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




import cv2
import numpy as np

# 读取图像
image = cv2.imread( 'image1.png', cv2.IMREAD_GRAYSCALE )  # 以灰度模式读取图像

# 定义不同的锐化卷积核
kernels = {
    'Custom_1': np.array( [[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]] ),

    'Prewitt_x': np.array( [[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]] ),
    'Prewitt_y': np.array( [[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]] ),

    'Sobel_x': np.array( [[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]] ),
    'Sobel_y': np.array( [[-1, -2, -1],
                          [0, 0, 0],
                          [1, 2, 1]] ),

    'Laplacian': np.array( [[0, -1, 0],
                            [-1, 4, -1],
                            [0, -1, 0]] ),

    'LoG': np.array( [[0, 0, -1, 0, 0],
                      [0, -1, -2, -1, 0],
                      [-1, -2, 16, -2, -1],
                      [0, -1, -2, -1, 0],
                      [0, 0, -1, 0, 0]] )
}

# 应用不同的卷积核custom
for kernel_name, kernel in kernels.items():
    sharpened_image = cv2.filter2D( image, -1, kernel )

    # 显示结果
    cv2.imshow( f'Sharpened Image - {kernel_name}', sharpened_image )

cv2.waitKey( 0 )
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt


def region_growing(image, seed):
    """
    区域生长算法
    :param image: 输入图像
    :param seed: 种子点
    :return: 分割结果图像
    """
    # 获取图像的高度和宽度
    height, width = image.shape

    # 创建一个与输入图像大小相同的标记图像，初始值为0
    segmented = np.zeros_like( image )

    # 设定生长阈值
    threshold = 50  # 可根据实际情况调整

    # 创建一个队列，用于存储待生长的像素坐标
    queue = []
    queue.append( seed )

    # 计算种子点的灰度值，作为生长的参考值
    reference_value = image[seed[0], seed[1]]

    # 定义8邻域
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while len( queue ) > 0:
        # 取出队列中的像素坐标
        current_point = queue.pop( 0 )

        # 将当前像素标记为已处理
        segmented[current_point[0], current_point[1]] = 255

        # 遍历8邻域
        for neighbor in neighbors:
            x = current_point[0] + neighbor[0]
            y = current_point[1] + neighbor[1]

            # 检查邻域像素是否在图像范围内
            if 0 <= x < height and 0 <= y < width:
                # 检查邻域像素是否已经被处理过
                if segmented[x, y] == 0:
                    # 检查邻域像素与参考值的灰度差异是否在阈值范围内
                    if abs( int( image[x, y] ) - int( reference_value ) ) < threshold:
                        # 将邻域像素加入队列，准备生长
                        queue.append( (x, y) )

    return segmented


# 读取图像
img = cv2.imread( "D:\\pycharmyunxing\\venv\\image1.png", 0 )

# 选择一个种子点（可以手动指定，也可以通过其他方法选择）
seed_point = (50, 50)

# 应用区域生长算法
result = region_growing( img, seed_point )

# 显示原始图像和区域生长结果
plt.subplot( 1, 2, 1 ), plt.imshow( img, cmap='gray' ), plt.title( '原始图像' )
plt.subplot( 1, 2, 2 ), plt.imshow( result, cmap='gray' ), plt.title( '区域生长结果' )
plt.show()

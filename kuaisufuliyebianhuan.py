import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("D:\\pycharmyunxing\\venv\\image1.png", 0)
f = np.fft.fft2(img)
fshift =np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum,cmap = 'gray')
plt.title('Magnitude_spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
'''图像进行二维傅立叶变换'''
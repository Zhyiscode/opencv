'''import cv2
import stitcher

imagea = cv2.imread("D:\\pycharmyunxing\\venv\\tu1.jpg")
imageb = cv2.imread("D:\\pycharmyunxing\\venv\\tu2.jpg")

stitcher = stitcher()
(result,vis) = stitcher.stitch([imagea,imageb],showMatches=True)

cv2.imshow("Image a",imagea)
cv2.imshow("Image b",imageb)
cv2.imshow("Keypoint Matches",vis)
cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import cv2
import sys
sys.path.append("Stitcher.py 所在的目录路径")
from Stitcher import Stitcher

imagea = cv2.imread("D:\\pycharmyunxing\\venv\\tu1.jpg")
imageb = cv2.imread("D:\\pycharmyunxing\\venv\\tu2.jpg")

stitcher = Stitcher()
(result, vis) = stitcher.stitch([imagea, imageb], showMatches=True)

cv2.imshow("Image a", imagea)
cv2.imshow("Image b", imageb)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()




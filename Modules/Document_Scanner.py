import cv2
import numpy as np

def run():
 img = cv2.imread('cards.jpg')

 resized = cv2.resize(img, (550,600))

 width , height = 250,350

 pts1 = np.float32([[2341,4169],[3766,3347],[3663,6487],[5133,5652]])
 pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

 matrix = cv2.getPerspectiveTransform(pts1,pts2)
 Output = cv2.warpPerspective(cv2.imread('cards.jpg'),matrix,(width,height))

 cv2.imshow("Original Image",resized)
 cv2.imshow("Scanned Image",Output)

 cv2.waitKey(0)
 cv2.destroyAllWindows()
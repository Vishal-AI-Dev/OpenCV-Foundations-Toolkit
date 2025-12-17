import cv2
import numpy as np

def run():
# Create a black image
 img = np.zeros((512,512,3),np.uint8)


 cv2.rectangle(img,(0,0),(350,250),(0,0,255),cv2.FILLED)
 cv2.circle(img,(450,460),50,(255,0,0),cv2.FILLED)
 cv2.putText(img,"CONFIDENTIAL",(100,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

#resize image
 img = cv2.resize(img,(400,400))

 cv2.imshow("Image",img)
 cv2.waitKey(0)



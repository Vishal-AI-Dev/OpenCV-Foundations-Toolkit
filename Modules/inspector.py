import cv2
import numpy as np

def run():
 cap = cv2.VideoCapture(0)
 cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
 cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
 cap.set(cv2.CAP_PROP_FPS,60)
 cap.set(cv2.CAP_PROP_BRIGHTNESS,150)
 cap.set(cv2.CAP_PROP_CONTRAST,50)  # CAP_PROP_CONTRAST
 cap.set(cv2.CAP_PROP_SATURATION,50)  # CAP_PROP_SATURATION



 while True:
    success, img = cap.read()
    if not success: # Check if frame is captured successfully
        print("Failed to capture image")
        break

    # Apply Canny edge detection
    cannyvideo = cv2.Canny(img, 100, 200) 

    # Apply Dilation to thicken the edges
    Kernel = np.ones((5,5),np.uint8)

    Dilationvideo = cv2.dilate(cannyvideo,Kernel,iterations=1)

    # Convert single channel images to BGR for display
    cmpcanny = cv2.cvtColor(cannyvideo, cv2.COLOR_GRAY2BGR)
    cmpdilation = cv2.cvtColor(Dilationvideo, cv2.COLOR_GRAY2BGR)

    # Resize each frame to 50% scale
    scale = 0.5
    img_small = cv2.resize(img, (0,0), None, scale, scale)
    canny_small = cv2.resize(cmpcanny, (0,0), None, scale, scale)
    dilated_small = cv2.resize(cmpdilation, (0,0), None, scale, scale)

    #Combining All 3 Outputs
    combined = np.hstack((img_small, canny_small, dilated_small))

    #cv2.imshow("Video", img)
    cv2.imshow("Dashboard", combined) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 cap.release()
 cv2.destroyAllWindows()

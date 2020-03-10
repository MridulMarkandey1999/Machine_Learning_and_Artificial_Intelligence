#for video streaming running code
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,photo=cap.read()
    cv2.imshow('hi' ,photo)
    if cv2.waitKey(1)==13:
        break 
cv2.destroyAllWindows()
cap.release()


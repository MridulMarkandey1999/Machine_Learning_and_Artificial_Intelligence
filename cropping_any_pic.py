#to see cropped photo
import cv2
x = cv2.VideoCapture(0)
status, photo = x.read()
cv2.imwrite('pic3.png', photo)
x.release()
nphoto = photo[50:350, 150:450]
cv2.imshow('hi' , nphoto)
cv2.waitKey()
cv2.destroyAllWindows()
    

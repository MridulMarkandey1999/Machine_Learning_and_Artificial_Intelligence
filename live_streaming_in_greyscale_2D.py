#code for live streaming in Grey image( 2-D image)
import cv2

cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade.xml')

#cv2.imwrite('photo.png', gphoto)
while True:
    ret, photo = cap.read()
    gphoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imshow('hi', gphoto)
    if cv2.waitKey(150) == 13:
        break
cv2.destroyAllWindows()    
cap.release()

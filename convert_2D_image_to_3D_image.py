#code for converting 3-D image(Coloured) to 2-D image(Grey)
import cv2
cap = cv2.VideoCapture(0)
ret, photo = cap.read()
gphoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
cv2.imwrite('photo.png', gphoto)
cap.release()

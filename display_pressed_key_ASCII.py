#for displaying keys number using waitkey
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()
    cv2.imshow('hi', photo)
    c = cv2.waitKey()
    print(c)
cv2.destroyAllWindows()
cap.release()

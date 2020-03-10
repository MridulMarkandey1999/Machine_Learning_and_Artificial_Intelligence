#to decrease the wide angle of video streaming
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()
    clphoto = photo[200:300, 250:350]
    #photo[0:100, 0:100] = clphoto
    cv2.imshow('hello', clphoto)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
cap.release()

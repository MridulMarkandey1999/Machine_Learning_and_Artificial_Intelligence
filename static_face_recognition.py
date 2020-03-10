#code for static face recognition
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()                    
    rphoto = cv2.rectangle(photo, (200,300), (400,100), (0,255,0), 2)                
    cv2.imshow('hi', rphoto)
    if cv2.waitKey(1) == 13:
        break
    else:
        cv2.imshow('hi', photo)
        if cv2.waitKey(1) == 13:
            break
cv2.destroyAllWindows()    
cap.release()

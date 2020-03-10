#code for face detection through green rectangular box
import cv2

face_model = cv2.CascadeClassifier('haarcascade.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()
    location = face_model.detectMultiScale(photo)
    if len(location) != 0:
        
            x1 = location[0][0]
            y1 = location[0][1]
            x2 = location[0][2] + x1
            y2 = location[0][3] + y1
                          
            photo = cv2.rectangle(photo, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.imshow('hi', photo)
            if cv2.waitKey(1) == 13:
                break
    else:
        cv2.imshow('hi', photo)
        if cv2.waitKey(1) == 13:
            break
cv2.destroyAllWindows()    
cap.release()

#code to crop 2-D image using face recognition

import cv2

cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade.xml')
while True:
    status, photo = cap.read()
    gphoto = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    location = face_model.detectMultiScale(photo)
    if len(location) != 0:
        
        x1 = location[0][0]
        y1 = location[0][1]
        x2 = location[0][2] + x1
        y2 = location[0][3] + y1
        
        nphoto = gphoto[y1:y2+1, x1:x2+1]
        cv2.imshow('hi', nphoto)
        if cv2.waitKey(1) == 13:
            break
    else:
        cv2.imshow('hi', gphoto)
        if cv2.waitKey(1) == 13:
            break
cv2.destroyAllWindows()    
cap.release()

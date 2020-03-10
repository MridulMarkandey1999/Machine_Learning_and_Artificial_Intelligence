#code to click and save 5 pics at a time

import cv2
cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier('haarcascade.xml')

for x in range(0, 5):
status, photo = cap.read()
location = face_model.detectMultiScale(photo)
if len(location) != 0:

x1 = location[0][0]
y1 = location[0][1]
x2 = location[0][2] + x1
y2 = location[0][3] + y1

photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
photo = photo[y1:y2, x1:x2]
#gphoto = cv2.rectangle(gphoto, (x1,y1), (x2,y2), (0,255,0), 2)
#cv2.imshow('hi', nphoto)
cv2.imwrite('image_dataset/sample1{}.png'.format(x), photo)
#if cv2.waitKey(1) == 13:
#  break
#else:
#   cv2.imshow('hi', gphoto)
#  if cv2.waitKey(1) == 13:
#     break

#cv2.destroyAllWindows()    
cap.release()

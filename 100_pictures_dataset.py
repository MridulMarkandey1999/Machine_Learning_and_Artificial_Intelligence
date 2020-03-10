import cv2

facemodle = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

for x in range(0, 1000):
    status, photo = cam.read()
    detect = facemodle.detectMultiScale(photo)
    cv2.imshow("gt",photo)
    if cv2.waitKey(1)==13:
        break
    if len(detect) != 0:
        x1 = detect[0][0]
        y1 = detect[0][1]
        x2 = detect[0][2] + x1
        y2 = detect[0][3] + y1
        cv2.rectangle(photo, (x1, y1), (x2, y2), (0,255,0), 2)
        cphoto = photo[y1:y2,x1:x2]
        rphoto = cv2.resize(cphoto, (200, 200))
        gphoto = cv2.cvtColor(rphoto, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('C:/Users/Mridul/Desktop/mridull/pic'+str(x)+'.png', gphoto)
        cv2.imshow("gt",photo)
        if cv2.waitKey(1)==13:
             break
cv2.destroyAllWindows()
cam.release()

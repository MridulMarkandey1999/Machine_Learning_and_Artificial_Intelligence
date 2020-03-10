# to see one green line in photo
import cv2
x = cv2.VideoCapture(0)
status, photo = x.read()
cv2.imwrite('pic3.png', photo)
x.release()
photo[10, 0:641] = [0,255,0]
cv2.imshow('hi' , photo)
cv2.waitKey()
cv2.destroyAllWindows()

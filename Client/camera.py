import cv2

cap = cv2.VideoCapture(0)

    # get a frame
ret, frame = cap.read()
    # show a frame
#cv2.imshow("capture", frame)
cv2.imwrite("/home/pi/test.jpg", frame)
        
cap.release()
cv2.destroyAllWindows()

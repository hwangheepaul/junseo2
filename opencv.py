import cv2

capture = cv2.VideoCapture(1,cv2.CAP_DSHOW)
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video',frame)
    
    if cv2.waitKey(20):
        break
capture.release()
cv2.destroyAllWindows()
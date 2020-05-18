import cv2

url ='http://root:pass@10.228.143.46/axis-cgi/mjpg/video.cgi'
cap = cv2.VideoCapture(url)
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

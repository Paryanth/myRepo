'''this is our videocam project'''
import cv2
'''opening up the camera'''   
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break 
cap.release()
'''release the resources'''
cv2.destroyAllWindows()

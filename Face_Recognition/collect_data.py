import numpy as np
import cv2

face_classifier = cv2.CascadeClassifier("/home/gc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")

def face_extractor(img):
	gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray,1.3,5)
		
	if faces is():
		return None
	for(x,y,w,h) in faces:
		print(x,y,w,h)
		cv2.imshow('face',img)
		cropped_face = img[y:y+h,x:x+w]
	return cropped_face

cap = cv2.VideoCapture(0)
count =0

while True:
	_,frame=cap.read()
	if face_extractor(frame) is not None:
		count+=1
		face = cv2.resize(face_extractor(frame),(200,200))
		face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

		file_path = "/home/gc/Desktop/Face_Recognition/data/face" +str(count)+".jpg"
		cv2.imwrite(file_path,face)
		cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
		cv2.imshow('face cropper',face)
	else:
		print('face Not Found')
		pass
	if cv2.waitKey(1) &0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
print('collecting samples Completed')

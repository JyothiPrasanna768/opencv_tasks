import cv2
import numpy as np
import os


data = '/home/gc/Desktop/Face_Recognition/data/'
Files = [f for f in os.listdir(data) if os.path.isfile(os.path.join(data,f))]

train_data, Labels = [], []

for i, files in enumerate(Files):
    image_path = data + Files[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    train_data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(train_data),np.asarray(Labels))

print(" Model Trained!!!!! ")

face_classifier = cv2.CascadeClassifier("/home/gc/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")

def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3 , 5)

    if faces is():
        return  img,[]

    for(x,y,w,h) in faces:
        cv2.rectangle(img , (x,y), (x+w,y+h) ,(0,255,255), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    return  img, roi

cap = cv2.VideoCapture(0)

while True :

    ret,frame = cap.read()

    image , face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))

        if confidence > 75:
            display_string = str(confidence) + '% confidence it is user'
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
            cv2.putText(image,"recognized" ,(250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Face Crop", image)
        else:
            cv2.putText(image, "not recognized",(250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Face Crop", image)

    except:
        cv2.putText(image, "Face Not Found",(250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Face Crop", image)
        pass

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

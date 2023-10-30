import cv2
import numpy as np

harcascade = "model/haarcascade_frontalface_default.xml"

camera = cv2.VideoCapture(0)  # 0 to use integrated camera

camera.set(3,640) # Width
camera.set(4,480) # height

while True:
    success,img = camera.read()  # if success is 2 only then i goes in next step

    face_cascade = cv2.CascadeClassifier(harcascade) # it accept grey scale images

    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # to convert into grey scale

    face = face_cascade.detectMultiScale(img_grey,1.1,4) # default parameters  to get (x,y,w,h)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)  # to create rectangle box with green color as RGB for colors(0,0,0) and 2 is for thickness

    cv2.imshow("Face",img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




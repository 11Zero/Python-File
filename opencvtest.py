# coding=utf-8
import cv2
import numpy as np
# img=cv2.imread('test.jpg')
# px=img[0:500,0:500]
# cv2.imshow('test',px)
# print(px)
# blue=img[100,100,0]
# print(blue)
imagepath="test.jpg"
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(
   gray,
   scaleFactor = 1.15,
   minNeighbors = 3,
   minSize = (5,5),
   # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print ("发现{0}个人脸!".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),1)
    # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

cv2.imshow("image",image)
# cv2.imshow("gray",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
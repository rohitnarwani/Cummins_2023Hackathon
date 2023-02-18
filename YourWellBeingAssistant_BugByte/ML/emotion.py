# -*- coding: utf-8 -*-
"""emotion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xpwei1rRXv6vevp30KD9VYottiv7Nt9i
"""

import cv2

pip install deepface

from deepface import DeepFace

img=cv2.imread('happyboy.jpeg')

import matplotlib.pyplot as plt

plt.imshow(img)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

predictions=DeepFace.analyze(img)

predictions

type(predictions)

print(predictions[0]['dominant_emotion'])

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  #to draw a rectangle around the face

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

font=cv2.FONT_HERSHEY_COMPLEX_SMALL 

cv2.putText(img,
            predictions[0]['dominant_emotion'],
            (0,50),
            font,3,
            (0,0,255),
             2,
            cv2.LINE_4);

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))


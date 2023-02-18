#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install deepface


# In[6]:


import cv2 
from deepface import DeepFace 


# In[7]:


import cv2
cv2.__version__


# In[8]:


import cv2

# Create a VideoCapture object for the default camera (0)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")

# Loop through frames from the camera
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    result = DeepFace.analyze (frame, actions = ['emotion'])
    faceCasCade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print (faceCascade.empty()) faces faceCascade.detectMultiScale (gray,1.1,4)
    faces=faceCasCade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    font= cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,
                result[0]['dominant_emotion'],
                (0,50),
                font,3,
                (0,0,255),
                2,
                cv2.LINE_4)
    cv2.imshow('Original video',frame) 

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break


    if ret:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





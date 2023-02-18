import winsound

import cv2
import dlib
import imutils
from imutils import face_utils
from scipy.spatial import distance


def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


count = 0


def drowsy1():
    thresh = 0.3
    frame_check = 20
    detect = dlib.get_frontal_face_detector()
    # Dat file is the crux of the code
    predict = dlib.shape_predictor("D:\\Stress1.5\\stress\\wocv\\shape_predictor_68_face_landmarks.dat")
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
    cap = cv2.VideoCapture(0)
    flag = 0
    i=100
    while i:
        count=0
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=900)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)  # converting to NumPy Array
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 256, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 256, 0), 1)
            if (ear < thresh):
                flag += 1
                if flag >= frame_check:
                    count = 1
                    cv2.putText(frame, "*****ALERT!*****",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 256), 2)
                    cv2.putText(frame, "DROWSY", (10, 300),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 256), 2)

            else:
                flag = 0
        i=i-1
        
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    
    cv2.destroyAllWindows()
    cap.release()
    return count
    


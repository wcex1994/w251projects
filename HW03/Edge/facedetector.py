
# Import Libraries 
import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt

# MQTT Host setting 
mosquitto_addr = "172.18.0.2"
client = mqtt.Client("localfacialrecognition")
client.connect(mosquitto_addr)
TOPIC = "hw03new"

# Capture Video
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Turn the framworks into grayscalemode
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Identify faces via Haar Cascades (Reference: https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html)
    face_cascade = cv.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:

        # Debugging 1: face 
        #face_img = frame[y:y+h,x:x+w]
        # print("Face Found!")
        #cv.imshow("image test",face_img)

        # Debugging 2: Video
        #cv2.imshow('frame',gray)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
        # cut out face from the frame
        face = frame[y:y+h,x:x+w]
        #print("Face Found",face.shape,face.dtype)
        rc,png = cv.imencode('.png', face)
        msg = png.tobytes()
        #print("messagesent: ",msg)
        client.publish(TOPIC,payload=msg)
        print("published messages!")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

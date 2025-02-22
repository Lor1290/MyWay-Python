import numpy as np
import cv2 as cv
import smtplib

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Video_1.avi', fourcc, 20.0, (640, 480))


while cap.isOpened():
   ret, frame = cap.read()
      
   if not ret:
         
      print(">>> Can't get the Output from the VideoCamera...")
      break

   out.write(frame)
   cv.imshow('frame', frame)

   if cv.waitKey(1) == ord('x'):
      break

cap.release()
cv.destroyAllWindows()
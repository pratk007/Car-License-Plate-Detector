import cv2
import numpy as np

frameWidth = 640    #Frame Width
frameHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("training.xml")
minArea = 500

capture =cv2.VideoCapture(0)
capture.set(3,frameWidth)
capture.set(4,frameHeight)
capture.set(10,150)
counting = 0

while True:
    success , img  = capture.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            # We are making a rectangle around the license plate to detect the numbers
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Put the text over the detected plate. 
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            # display our region of interest
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("Images"+str(counting)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        counting+=1

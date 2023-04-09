import cv2
import numpy as np
import time
import imutils
import sys
import pytesseract
import pandas as pd
import subprocess as sp

programname="Notepad.exe"
filename="file_name1.txt"
sp.Popen([programname,filename])
def ratioCheck(area, width, height):
    ratio = float(width) / float(height)
    if ratio < 1:
        ratio = 1 / ratio
    if (area < 1063.62 or area > 73862.5) or (ratio < 3 or ratio > 6):
        return False
    return True
def isMaxWhite(plate):
    avg = np.mean(plate)
    if(avg>=115):
        return True
    else:
         return False
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

frameWidth = 640    #Frame Width
frameHeight = 480   #Frame Height

plateCascade = cv2.CascadeClassifier(r"C:\Users\Dell\PycharmProjects\pythonProject4\haarcascade_russian_plate_number1.xml")
minArea = 500

cap =cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
count = 0
while True:
    success,img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
# configuration for tesseract
    config = ('-l eng --oem 1 --psm 3')

    # run tesseract OCR on image
    text = pytesseract.image_to_string(img, config=config)
    print(text)

    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite(r"C:\Users\Dell\PycharmProjects\pythonProject4\SATHYA\cascade\IMAGES"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)


        def wordcount(file_name1, listwords):
            try:
                file = open(file_name1, "r")
                read = file.readlines()
                file.close()
                for word in listwords:
                    lower = word.lower()
                    count = 0
                    for sentance in read:
                        line = sentance.split()
                        for each in line:
                            line2 = each.lower()
                            line2 = line2.strip("!@#$%^&*()_+=")
                            if lower == line2:
                                count += 1
                    print(lower, ":", count)
            except FileExistsError:
                print("Number not Found")


        wordcount("file_name1.txt", ["HR26DK8337"])
        print("Number is Found")

        cv2.waitKey(500)
        count+=1



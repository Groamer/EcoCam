#!/usr/bin/python

__author__ = 'Tom Remeeus'

import cv2
import datetime
from time import sleep

def openCamera():
    print("Opening camera...")
    
    #force camera to open
    while(True):
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            print("Camera opened.")
            break
        
        sleep(1)
        
    return cap
        
def takePicture(cap):
    ret, picture = cap.read()      
    
    return picture

def countContours(img):
    #edit picture
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retT, thresh = cv2.threshold(gray, 40, 200, cv2.THRESH_BINARY_INV)
    retC, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #count contours
    count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        #only count big contours
        if area > 250:
            count = count + 1
    
    return count
    
def takeVideo(cap):
    print("Motion detected, start filming")
    
    #set params for file format
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(getFileName(), fourcc, 20.0, (640, 480))
    
    #attached Logitech cam records with 20fps
    #20 * 60 = 1200 frames = 1 minut
    for i in range(0, 100):
        ret, frame = cap.read()
        
        if ret == True:
            out.write(frame)
        
        #show recording
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
        
def getFileName():
    #get date and set date as file name
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    format = ".avi"
    
    fileName = date + format
    return fileName

def main():
    #init camera
    cam = openCamera()
    
    #take first picture as reference
    old = countContours(takePicture(cam))
    
    while(True):
        sleep(2)
        new = countContours(takePicture(cam))
        
        #if the amount of contour differ, start filming
        if old != new:
            takeVideo(cam)
            old = countContours(takePicture(cam))
        else:
            old = new

main()
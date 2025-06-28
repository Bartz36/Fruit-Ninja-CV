import cv2
import numpy as np
import mediapipe as mp4
import pyautogui
from pynput.mouse import Controller
from cvzone.HandTrackingModule import HandDetector


videoCapture = cv2.VideoCapture(0)

camWidth, camHeight = 640, 480
videoCapture.set(3, camWidth)
videoCapture.set(4, camHeight)
frameReduction = 100

handDetector = HandDetector(detectionCon=0.65, maxHands=1)
mouse = Controller()
screen_width, screen_height = pyautogui.size()

while True:
    success, image = videoCapture.read()
    image = cv2.flip(image, 1)
    hands, image = handDetector.findHands(image)
    cv2.rectangle(image, (frameReduction, frameReduction), (camWidth - frameReduction, camHeight - frameReduction), (255, 0, 255), 2)
    
    if hands:
        lmList = hands[0]['lmList'] 
        index_x, index_y = lmList[8][0], lmList[8][1]
        
        #create circle on index finger (represents the mouse)
        cv2.circle(image, (index_x, index_y), 20, (0, 255, 255), 2)

        convert_x = int( np.interp(index_x, (frameReduction, camWidth - frameReduction), (0, screen_width)))
        convert_y = int( np.interp(index_y, (frameReduction, camHeight - frameReduction), (0, screen_height)) )
        mouse.position = (convert_x, convert_y)

    
    
    cv2.imshow("Video Feed", image)
    cv2.waitKey(1)


